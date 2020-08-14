import cv2
import numpy as np

kernel = np.ones((5, 5), dtype=np.uint8)
img = cv2.imread('dataset/images/sample_img.jpg')

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey, (7, 7), 0)
img_canny = cv2.Canny(img, 200, 200)
img_dilated = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_dilated, kernel, iterations=1)

cv2.imshow('Original', img)

cv2.imshow('Grey', img_grey)
cv2.imshow('Blur', img_blur)
cv2.imshow('Canny Edge', img_canny)
cv2.imshow('Dilated', img_dilated)
cv2.imshow('Eroded', img_eroded)
cv2.waitKey(0)


img = cv2.imread('dataset/images/sample_img.jpg')
print(img.shape)

img_resize = cv2.resize(img, (300, 400))
print(img_resize.shape)

img_cropped = img[150:550, 20:250]
print(img_cropped.shape)

#cv2.imshow('Original', img)

cv2.imshow('Resized', img_resize)
cv2.imshow('Cropped', img_cropped)
cv2.waitKey(0)