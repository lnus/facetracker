import face_recognition
import cv2
import numpy as np
import random

video_capture = cv2.VideoCapture(0)

face_landmarks_list = []

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)

    #TODO: Add some compression for faster processing

    face_landmarks_list = face_recognition.face_landmarks(frame)

    for face_landmarks in face_landmarks_list:
        facial_features = [
            'chin',
            'left_eyebrow',
            'right_eyebrow',
            'nose_bridge',
            'nose_tip',
            'left_eye',
            'right_eye',
            'top_lip',
            'bottom_lip'
        ]

        # Draw the chin
        for facial_feature in facial_features:
            points = []
            for point in face_landmarks[facial_feature]:
                points.append(point)
            for i in range(len(points)-1):
                cv2.line(frame, points[i], points[i+1], (random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)), 5)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
