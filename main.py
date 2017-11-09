import face_recognition
import cv2

video_capture = cv2.VideoCapture(1)

face_locations = []
render_faces = True
optimized_mode = False

while True:
    ret, frame = video_capture.read()

    if render_faces:
        # Compresses frame for faster processing (better framerate)
        # Downscale by 4
        compressed_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        face_locations = face_recognition.face_locations(compressed_frame)

    for (top, right, bottom, left) in face_locations:
        # Multiply by 4 since we downscaled by 4 on the face locator
        cv2.rectangle(frame, (left*4,top*4), (right*4, bottom*4), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    # Switch for every other frame
    if optimized_mode:
        render_faces = not render_faces

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Drops cam
video_capture.release()
cv2.destroyAllWindows()
