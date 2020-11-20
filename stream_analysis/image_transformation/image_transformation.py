from IPython.display import Image
import numpy as np
from cv2 import cv2
import os
import PIL
import matplotlib.pyplot as plt

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),20,(255,0,0),-1)
        mouseX,mouseY = x,y

# print(M)

# plt.rcParams["figure.figsize"]= 10,10

# plt.imshow(img)
# plt.title('Input')
# plt.show()

# plt.imshow(dst)
# plt.title('Output')
# plt.show()

def calc_matrix():

    #TODO replace with reading image from camera
    filepath = os.path.join(os.getcwd(), "stream_analysis","image_transformation","sample_pictures","2-high.jpg")
    image = PIL.Image.open(filepath)
    width, height = image.size
    print(width, height)

    img = cv2.imread(filepath)
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", 600,600)
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
    
    #img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # set CV2 color scale to RGB
    rows,cols,ch = img.shape

    pts1 = np.float32([pos_blue,pos_red,pos_yellow])
    pts2 = np.float32([[1001, 1173],[1750, 1616],[3031, 1236]]) #TODO move to config?

    M = cv2.getAffineTransform(pts1,pts2)

    return M

def apply_matrix_to_pt(pos, M, (rows, columns)):

    #TODO Magnus Morales Magic
    # np.matmul(M, pos) ?

    return pos_transformed

def apply_matrix_to_img(img, M, (rows, columns)):

    return cv2.warpAffine(img,M,(cols,rows))