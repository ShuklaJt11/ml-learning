import cv2
import numpy as np

def get_contours(img):
    contours, heirarchy = cv2.findContours(image=img, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    min_area = 500
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > min_area:
            cv2.drawContours(image=img_copy, contours=cnt, contourIdx=-1, color=(255, 0, 0), thickness=1)
            pmt = cv2.arcLength(curve=cnt, closed=True)
            appx = cv2.approxPolyDP(curve=cnt, epsilon=0.04 * pmt, closed=True)
            obj_cornors = len(appx)
            x, y, width, height = cv2.boundingRect(array=appx)

            obj_type = ''
            if obj_cornors == 3: obj_type = 'Triangle'
            elif obj_cornors == 4:
                aspect_ratio = width / float(height)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05: obj_type = 'Square'
                else: obj_type = 'Rectangle'
            elif obj_cornors > 4:
                obj_type = 'Circle'

            cv2.rectangle(img=img_copy, pt1=(x, y), pt2=(x + width, y + height), color=(0, 0, 255), thickness=2)
            cv2.putText(img=img_copy, text=obj_type, org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.65, color=(0, 0, 0), thickness=1)


img = cv2.imread('dataset/images/shapes.png')
img_copy = cv2.GaussianBlur(src=img, ksize=(19, 19), sigmaX=0)

img_grey = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(src=img_grey, ksize=(7, 7), sigmaX=0)
img_canny = cv2.Canny(img_blur, 50, 50)

get_contours(img_canny)

cv2.imshow('Original', img)
cv2.imshow('Contours', img_copy)
cv2.waitKey(0)