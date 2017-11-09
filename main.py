import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

render_faces = True

while True:
    ret, frame = video_capture.read()

    if render_faces:
        # Compresses frame for faster processing
        compressed_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

        face_locations = face_recognition.face_locations(compressed_frame)

        for (top, right, bottom, left) in face_locations:
            print(top, right, bottom, left)
            cv2.rectangle(frame, (left,top), (right, bottom), (0,0, 255), 2)

    cv2.imshow('Video', frame)

    # Switch for every other frame
    render_faces = not render_faces

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Drops cam
video_capture.release()
cv2.destroyAllWindows()
