import cv2
import numpy as np

img = cv2.imread('dataset/images/cards.jpg')

width, height = 250, 350

pts1 = np.float32([[460, 370], [542, 190], [700, 226], [630, 420]])
pts2 = np.float32([[0, height], [0, 0], [width, 0], [width, height]])

matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)

img_warped = cv2.warpPerspective(src=img, M=matrix, dsize=(width, height))

cv2.imshow('Image', img)
cv2.imshow('Warped image', img_warped)
cv2.waitKey(0)