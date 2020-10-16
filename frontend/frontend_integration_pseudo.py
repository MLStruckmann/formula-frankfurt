class Detector(object):
    def __init__(self):
        # all the shit you run once

    # def __del__(self):
    #     self.video.release()

    def get_frame(path, img, im0s, vid_cap):
        
        ...

        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()#, quant data

    # def get_quant...


def gen(detector):

    for path, img, im0s, vid_cap in dataset:
        frame = detector.get_frame(path,img,im0s,vid_cap)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
