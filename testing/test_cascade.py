import cv2

haar = cv2.CascadeClassifier('../data/firetruck_cascade.xml')
img = cv2.imread('test.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = haar.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('output.png',img)
