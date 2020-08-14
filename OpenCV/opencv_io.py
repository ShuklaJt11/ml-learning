import cv2

# For images
img = cv2.imread('dataset/images/IMG_20200530_160628.jpg')
cv2.imshow('Output Window Title', img)

cv2.waitKey(0)


# For videos
vid_capture = cv2.VideoCapture('dataset/videos/sample_video.mp4')

while True:
    success, img = vid_capture.read()
    if not success:
        break

    cv2.imshow("Our Video Title", img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


# For WebCam
vid_capture = cv2.VideoCapture(0) # 0 uses the default camera of the laptop. If multiple webcams are connected we can use camera ID
vid_capture.set(3, 640) # 3 is the ID number for width
vid_capture.set(4, 480) # 4 is the ID number for height
vid_capture.set(10, 100) # 10 is the Brightness setting

while True:
    success, img = vid_capture.read()
    if not success:
        break

    cv2.imshow("Our Video Title", img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break