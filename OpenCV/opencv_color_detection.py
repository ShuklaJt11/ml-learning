import cv2
import numpy as np

# Original image
img = cv2.imread('dataset/images/sample_img.jpg')
# Create a trackbar for tracking hue values

# Define an empty function to pass into trackbar
def empty(dummy):
    pass

# Create trackbar
cv2.namedWindow(winname='TrackBars')
cv2.resizeWindow(winname='TrackBars', width=640, height=240)
cv2.createTrackbar('Hue Min', 'TrackBars', 96, 179, empty) # 0 is the default value and the count 179 is used as OpenCv can have 180 (0-179) different hue values 
cv2.createTrackbar('Hue Max', 'TrackBars', 135, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBars', 71, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBars', 132, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBars', 55, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBars', 166, 255, empty)


while True:
    img_hsv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos(trackbarname='Hue Min', winname='TrackBars')
    h_max = cv2.getTrackbarPos(trackbarname='Hue Max', winname='TrackBars')
    s_min = cv2.getTrackbarPos(trackbarname='Sat Min', winname='TrackBars')
    s_max = cv2.getTrackbarPos(trackbarname='Sat Max', winname='TrackBars')
    v_min = cv2.getTrackbarPos(trackbarname='Val Min', winname='TrackBars')
    v_max = cv2.getTrackbarPos(trackbarname='Val Max', winname='TrackBars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(src=img_hsv, lowerb=lower, upperb=upper)
    img_out = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original', img)
    #cv2.imshow('HSV', img_hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('OutPut', img_out)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break