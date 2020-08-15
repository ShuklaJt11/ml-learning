import cv2
import numpy as np

img = cv2.imread('dataset/images/sample_img.jpg')
img_grey = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(src=img_grey, ksize=(7, 7), sigmaX=0)
img_canny = cv2.Canny(image=img, threshold1=200, threshold2=200)

horizontal = np.hstack((img_grey, img_blur, img_canny))
vertical = np.vstack((img_grey, img_blur, img_canny))

cv2.imshow('Horizontal', horizontal)
cv2.imshow('Vertical', vertical)
cv2.waitKey(0)