import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)

    for (top, right, bottom, left) in face_locations:
        print(top, right, bottom, left)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Drops cam
video_capture.release()
cv2.destroyAllWindows()
