from flask import Flask, Response
import cv2
import os
import argparse

from maindash import recent_locations, get_config
from stream_analysis.motion_detection.models import *  # set ONNX_EXPORT in models.py
from stream_analysis.motion_detection.utils.datasets import * 
from stream_analysis.motion_detection.utils.utils import *

class Detector(object):

    def __init__(self,weights_arg,cfg_arg,names_arg,device_arg,source_arg,save_img=False):

        self.weights = weights_arg
        self.cfg = cfg_arg
        self.source = source_arg
        self.names = names_arg
        self.device = device_arg
        self.webcam = self.source == '0' or self.source.startswith('rtsp') or self.source.startswith('http') or self.source.endswith('.txt')
        print('in')

        self.imgsz = 512
        self.out = 'output'
        self.half = False
        self.view_img = False
        self.save_txt = False
        self.augment = False
        self.agnostic_nms = False
        self.classes = None
        self.conf_thres = 0.3
        self.fourcc = 'mp4v'
        self.iou_thres = 0.6

        # Initialize
        self.device = torch_utils.select_device(device=self.device)
        if os.path.exists(self.out):
            shutil.rmtree(self.out)  # delete output folder
        os.makedirs(self.out)  # make new output folder
        # Initialize model
        self.model = Darknet(self.cfg, self.imgsz)

        # Load weights
        if self.weights.endswith('.pt'):  # pytorch format
            self.model.load_state_dict(torch.load(self.weights, map_location=self.device)['model'])
        else:  # darknet format
            load_darknet_weights(self.model, self.weights)

        # Second-stage classifier
        self.classify = False
        if self.classify:
            self.modelc = torch_utils.load_classifier(name='resnet101', n=2)  # initialize
            self.modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=self.device)['model'])  # load weights
            modelc.to(self.device).eval()

        # Eval mode
        self.model.to(self.device).eval()
        
        # Fuse Conv2d + BatchNorm2d layers
        # model.fuse()

        # Half precision
        self.half = self.half and self.device.type != 'cpu'  # half precision only supported on CUDA
        if self.half:
            self.model.half()

        # Set Dataloader
        self.vid_path, self.vid_writer = None, None
        if self.webcam:
            self.view_img = True
            torch.backends.cudnn.benchmark = True  # set True to speed up constant image size inference
            self.dataset = LoadStreams(self.source, img_size=self.imgsz)
        else:
            self.save_img = True
            self.dataset = LoadImages(self.source, img_size=self.imgsz)

        # Get names and colors
        self.names = load_classes(self.names)
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(self.names))]

        # Run inference
        t0 = time.time()
        self.img = torch.zeros((1, 3, self.imgsz, self.imgsz), device=self.device)  # init img
        _ = self.model(self.img.half() if self.half else self.img.float()) if self.device.type != 'cpu' else None  # run once
        print(self.dataset)


    def get_frame(self,path, img, im0s, vid_cap):
        img = torch.from_numpy(img).to(self.device)
        img = img.half() if self.half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = torch_utils.time_synchronized()
        pred = self.model(img, augment=self.augment)[0]
        t2 = torch_utils.time_synchronized()

        # to float
        if self.half:
            pred = pred.float()

        # Apply NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres,
                                   multi_label=False, classes=self.classes, agnostic=self.agnostic_nms)

        # Apply Classifier
        if self.classify:
            pred = apply_classifier(pred, self.modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections for image i
            label_det = []
            if self.webcam:  # batch_size >= 1
                p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
            else:
                p, s, im0 = path, '', im0s

            save_path = str(Path(self.out) / Path(p).name)
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  #  normalization gain whwh
            if det is not None and len(det):
                # Rescale boxes from imgsz to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].detach().unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += '%g %ss, ' % (n, self.names[int(c)])  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    if self.save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        with open(save_path[:save_path.rfind('.')] + '.txt', 'a') as file:
                            file.write(('%g ' * 5 + '\n') % (cls, *xywh))  # label format

                    if self.view_img:  # Add bbox to image
                        label = '%s %.2f' % (self.names[int(cls)], conf)
                        label_det.append(label)
                        plot_one_box(xyxy, im0, label=label, color=self.colors[int(cls)])

            label_det.reverse()
            # Stream results
            if self.view_img:
                return (p, im0, det, label_det)


def gen(camera):

    for path, img, im0s, vid_cap in camera.dataset:
        (p, im0, det, labels) = camera.get_frame(path, img, im0s, vid_cap)
        
        if det is not None:
            
            for i in range(len(labels)):
                
                cl = 'green'  
                if labels[i].split(' ')[0] == 'black_car':
                    cl = 'black'
                else: cl = 'red'

                recent_locations.pop(0)
                recent_locations.append((int(det[i][0]), int(det[i][1]), cl))

        config = get_config()
        dim = tuple(config["camera_aspect_ratio"])
        im0 = cv2.resize(im0, dim, interpolation = cv2.INTER_AREA)
        _ , jpeg = cv2.imencode('.jpg', im0)
        frame = jpeg.tobytes()
     
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
