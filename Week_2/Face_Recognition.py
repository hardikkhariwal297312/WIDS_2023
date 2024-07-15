import cv2
import face_recognition
import os

# Function to recognize faces from the webcam
def recognize_faces_webcam():
    # Load face encodings for known faces (you need to prepare this in advance)
    # Replace "known_faces" with a dictionary where keys are names and values are face encodings
    known_faces = {
        "Swarup": face_recognition.face_encodings(face_recognition.load_image_file(r"Swar.jpg"))[0]
        # "Hardik": face_recognition.face_encodings(face_recognition.load_image_file(r"C:\Users\91797\Desktop\New folder\pic\WhatsApp Image 2023-12-25 at 02.16.15_e7815314.jpg"))[0],
        # Add more known faces as needed
    }

    # Open the webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture each frame from the webcam
        frame = video_capture.read()

        # Find all face locations and face encodings in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)

            name = "Unknown"  # Default to "Unknown" if no match is found

            # If a match is found, use the name of the known face
            if True in matches:
                first_match_index = matches.index(True)
                name = list(known_faces.keys())[first_match_index]

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

# Call the function to start facial recognition from the webcam
recognize_faces_webcam()


