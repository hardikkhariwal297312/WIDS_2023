import numpy as np
import cv2

# Load the image and resize it for better display
img = cv2.imread(r"Example-face-forward-pictures-From-left-to-right-top-to-bottom-anger-contempt.png")
img = cv2.resize(img, (640, 800))

# Create a Preprocessing function to apply necessary operations on the input image
def preProcessing(img):
    # Convert image to grayscale
    imgPre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply blur to the image
    imgPre = cv2.blur(imgPre, (15, 15), 0)
    
    return imgPre

# Call preprocessing function
imgPre = preProcessing(img)

# Load the Haar Cascade Classifier for face detection
H_C = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detect faces in the preprocessed image
F_R = H_C.detectMultiScale(imgPre, scaleFactor=1.1, minNeighbors=3)

# Print the number of faces found in the picture
print("Number of Faces in picture:", len(F_R))

# Draw rectangles around the detected faces
for (x, y, w, h) in F_R:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

# Display the image with rectangles around detected faces
cv2.imshow("Image", img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
