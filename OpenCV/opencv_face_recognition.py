import cv2

face_cascade_classifier = cv2.CascadeClassifier('dataset/cascades/haarcascade_frontalface_default.xml')

# For single image
face_img = cv2.imread('dataset/images/face.jpg')
face_img = cv2.resize(src=face_img, dsize=(800, 600))

face_img_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade_classifier.detectMultiScale(image=face_img_gray, scaleFactor=1.1, minNeighbors=4)

for face in faces:
    x, y, width, height = face
    cv2.rectangle(img=face_img, pt1=(x, y), pt2=(x + width, y + height), color=(0, 0, 255), thickness=2)

cv2.imshow('Result', face_img)
cv2.waitKey(0)

# For WebCam
vid_capture = cv2.VideoCapture(1) # 0 uses the default camera of the laptop. If multiple webcams are connected we can use camera ID
vid_capture.set(3, 1280) # 3 is the ID number for width
vid_capture.set(4, 720) # 4 is the ID number for height
vid_capture.set(10, 150) # 10 is the Brightness setting

while True:
    success, face_img = vid_capture.read()
    
    if not success:
        break

    face_img_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade_classifier.detectMultiScale(image=face_img_gray, scaleFactor=1.1, minNeighbors=4)
    for face in faces:
        x, y, width, height = face
        cv2.rectangle(img=face_img, pt1=(x, y), pt2=(x + width, y + height), color=(0, 0, 255), thickness=2)

    cv2.imshow("Face Recognition with webcam", face_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break