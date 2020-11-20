from IPython.display import Image
import numpy as np
from cv2 import cv2, VideoCapture
import os
import PIL
import matplotlib.pyplot as plt

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y

# print(M)

# Print example transformation from picture #
#############################################

# plt.rcParams["figure.figsize"]= 10,10

# plt.imshow(img)
# plt.title('Input')
# plt.show()

# plt.imshow(dst)
# plt.title('Output')
# plt.show()

def calc_matrix():

    global img
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    print(img.shape)
    #TODO replace with reading image from camera
    #filepath = os.path.join(os.getcwd(),"src","stream_analysis","image_transformation","sample_pictures","2-high.jpg")
    #print(filepath)
     
    #img = cv2.imread(filepath)
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", 1280,720)
    cv2.setMouseCallback("image",draw_circle)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == ord("p"):
            print(mouseX,mouseY)
        elif k == ord("b"):
            pos_blue = [mouseX,mouseY]
        elif k == ord("r"):
            pos_red = [mouseX,mouseY]
        elif k == ord("y"):
            pos_yellow = [mouseX,mouseY]
        elif k == ord("q"):
            cv2.destroyAllWindows()
            break

    # TODO: Error Handling
    # try:
    #     pos_blue
    #     pos_red
    #     pos_yellow
    # except NameError:
    #     print("Not all points were assigned")
    # else:
    #     print(pos_blue)
    #     print(pos_red)
    #     print(pos_yellow)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # set CV2 color scale to RGB
    rows,cols,ch = img.shape

    pts1 = np.float32([pos_blue,pos_red,pos_yellow])
    pts2 = np.float32([[1001, 1173],[1750, 1616],[3031, 1236]]) #TODO move to config?

    M = cv2.getAffineTransform(pts1,pts2)

    return M

def transform_point(M, pos):

    pos.append(1)
    return np.matmul(M,pos)

def transform_image(M, img, img_size):
    
    pass
    #return cv2.warpAffine(img,M,(cols,rows))