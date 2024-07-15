import cv2
import os
from datetime import datetime
import face_recognition
import csv

def add_new_face(known_faces, user_id, frame):
    # Get the user's name
    user_name = input("Enter your name: ")

    # Save the photo with the user's ID as the filename
    photo_filename = f"{user_id}.jpg"
    photo_path = os.path.join(save_folder, photo_filename)
    cv2.imwrite(photo_path, frame)

    # Load the newly added face encoding
    new_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file(photo_path))[0]

    # Add the new face to the known_faces dictionary
    known_faces[user_name] = new_face_encoding

    print(f"New face added: {user_name}")

# Function to take and save photos
def take_and_save_photo(save_folder, known_faces):
    # Open the video capture object for the webcam
    video_capture = cv2.VideoCapture(0)

    # Create the save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Display instructions to the student
    print("Welcome to the Attendance Registration System!")
    print("Please follow the instructions below:")
    print("1. Look directly into the camera.")
    print("2. Enter your name and user ID when prompted.")
    print("3. Press the spacebar to capture your photo.")
    print("4. Press 'q' to quit the program.")

    while True:
        # Capture each frame from the webcam
        ret, frame = video_capture.read()

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Wait for the user to press the spacebar to capture a photo
        key = cv2.waitKey(1)
        if key == 32:  # ASCII code for spacebar
            # Get user's name and user ID
            user_name = input("Enter your name: ")
            user_id = input("Enter your user ID: ")

            # Check if the student is already in the known_faces dictionary
            if user_name in known_faces:
                print(f"User {user_name} already registered.")
            else:
                # Get the current timestamp for the photo filename
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                photo_filename = f"{user_id}.jpg"

                # Save the photo to the specified folder
                photo_path = os.path.join(save_folder, photo_filename)
                cv2.imwrite(photo_path, frame)

                print(f"Photo saved: {photo_path}")

                # If the student is not in the list, add them to the known_faces dictionary
                add_new_face(known_faces, user_id, frame)

        # Break the loop if the user presses 'q'
        elif key == ord('q'):
            break

    # Release the video capture object and close the window
    video_capture.release()
    cv2.destroyAllWindows()

# Function to recognize faces from the webcam and log attendance
def recognize_faces_webcam(save_folder, known_faces):
    # Open the webcam
    video_capture = cv2.VideoCapture(0)

    # Open CSV file for writing attendance
    with open('attendance.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header to the CSV file
        writer.writeheader()

        # Display instructions to the student
        print("Welcome to the Attendance Marking System!")
        print("Please follow the instructions below:")
        print("1. Look directly into the camera.")
        print("2. Press 'p' to mark attendance when prompted.")
        print("3. Press 'q' to quit the program.")
        print("Make sure your face is well-lit and visible to the camera.")
        print("-------------------------------")

        while True:
            # Capture each frame from the webcam
            ret, frame = video_capture.read()

            # Find all face locations and face encodings in the frame
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            # Loop through each face found in the frame
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Check if the face matches any known faces
                matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)

                # If a match is found, log the attendance on 'p' key press
                if True in matches and cv2.waitKey(1) & 0xFF == ord('p'):
                    first_match_index = matches.index(True)
                    name = list(known_faces.keys())[first_match_index]

                    # Get the current time
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Write the attendance to the CSV file
                    writer.writerow({'Name': name, 'Time': current_time})

                    # Draw a rectangle around the face and display the name
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, f"{name} - {current_time}", (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

                    # Display a success message on the video feed
                    cv2.putText(frame, "Attendance marked successfully!", (50, 50), font, 1, (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the webcam and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    save_folder = "Pictures"  # Replace with your desired folder name
    known_faces = {}  # Dictionary to store known faces and encodings

    # Call the function to take and save photos
    take_and_save_photo(save_folder, known_faces)

    # Call the function to recognize faces and mark attendance
    recognize_faces_webcam(save_folder, known_faces)
