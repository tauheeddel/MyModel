import cvzone
import cv2

cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('MyModel/keras_model.h5', 'MyModel/labels.txt')


while True:
    _, img = cap.read()
    predictions = myClassifier.get_predictions(img)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)