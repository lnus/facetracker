import face_recognition
import cv2

video_capture = cv2.VideoCapture(1)

# For testing
image_of_me = face_recognition.load_image_file("images/me.jpg") # Place your own file here :)
my_face_encoding = face_recognition.face_encodings(image_of_me)[0]

face_locations = []
face_encodings = []
face_names = []
render_faces = True
optimized_mode = True
use_face_encodings = True # Detects who is in the frame, slows down the software by like 99%

while True:
    ret, frame = video_capture.read()

    # Mirrors the camera for a more natural, mirror-like, feel
    frame = cv2.flip(frame, 1)

    if render_faces:
        # Compresses frame for faster processing (better framerate)
        # Downscale by 4
        compressed_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        face_locations = face_recognition.face_locations(compressed_frame)
        face_names = []
        if use_face_encodings:
            face_encodings = face_recognition.face_encodings(compressed_frame, face_locations)
            for face_encoding in face_encodings:
                # Look for a match
                match = face_recognition.compare_faces([my_face_encoding], face_encoding)
                name = "Unknown"
                if match[0]:
                    name = "Me"
                face_names.append(name)

    # Draw the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Multiply by 4 since we downscaled by 4 on the face locator
        top *= 4
        right *= 4
        left *= 4
        bottom *=4

        # Draw a box around the faces
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 5)

        # Draw the name below the face
        if not name: name = "Unknown" # In case 'use_face_encodings' is False
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left+6, bottom), font, 1.0, (0,0,0), 1)

    cv2.imshow('Video', frame)


    # Switch for every other frame
    if optimized_mode:
        render_faces = not render_faces

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Drops cam when finished
video_capture.release()
cv2.destroyAllWindows()
