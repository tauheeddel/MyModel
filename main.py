#Trained Model Using https://teachablemachine.withgoogle.com/train/image

import cvzone
import cv2

cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('MyModel/keras_model.h5', 'MyModel/labels.txt')


while True:
    _, img = cap.read()
    predictions = myClassifier.getPrediction(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)