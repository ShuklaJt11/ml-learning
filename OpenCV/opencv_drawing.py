import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
# img[:] = 255, 0, 0 # OpenCV works with BGR values by default

cv2.line(img=img, pt1=(100, 100), pt2=(400, 400), color=(0, 255, 0), thickness=2)
cv2.rectangle(img=img, pt1=(100, 100), pt2=(400, 400), color=(0, 255, 255), thickness=2)
cv2.circle(img=img, center=(img.shape[1] // 2, img.shape[0] // 2), radius=100, color=(0, 0, 255), thickness=2)
cv2.putText(img=img, text='Damn!', org=(50, 50), fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=2, color=(255, 0, 255), thickness=1)

cv2.imshow('Image', img)
cv2.waitKey(0)