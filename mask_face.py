import face_recognition
import cv2
import numpy as np
import random

video_capture = cv2.VideoCapture(0)

face_landmarks_list = []
compressed_mode = False # False = Better accuracy, True = Faster speeds

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)

    compute_frame = frame
    compressed_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    if compressed_mode: compute_frame = compressed_frame
    face_landmarks_list = face_recognition.face_landmarks(compute_frame)

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
            # Scales up the points with 4, since the image was scaled down by 4
            points = []
            for point in face_landmarks[facial_feature]:
                if compressed_mode:
                    new_point = (point[0]*4, point[1]*4)
                else:
                    new_point = point
                points.append(new_point)
            for i in range(len(points)-1):
                cv2.line(frame, points[i], points[i+1], (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 5)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
