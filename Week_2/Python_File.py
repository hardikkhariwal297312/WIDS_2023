import numpy as np
import cv2
import cvzone

img = cv2.imread("one.jpg")
img = cv2.resize(img, (640, 800))


# Creat a Preprocessing function to apply necessary operations on the input image
def preProcessing(img):
    
    # Convert image to grayscale
    imgPre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply blur to the image
    imgPre = cv2.blur(img, (15, 15), 0)
    
    
    # Apply Canny edge detection
    imgPre = cv2.Canny(imgPre, 20, 20)
    # Apply dilation and morphological closing
    kernel = np.ones((3, 3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
    return imgPre

# Call preprocessing function
imgPre = preProcessing(img)

# Find contours in the preprocessed image
imgContours, conFound = cvzone.findContours(img, imgPre, minArea=2000)

    
# Stack the images for display
imgStacked = cvzone.stackImages([ img, imgPre, imgContours], 2, 0.5)

#Create a dictionary to store contour areas
area = {}
arc_length={}
#Calculate and store the area of each contour
for i in range(len(conFound)):
    cnt = conFound[i]
    ar = cv2.contourArea(cnt['cnt'], True)
    arclen=cv2.arcLength(cnt['cnt'], True)
    area[i] = np.abs(ar)
    arc_length[i]=np.abs(arclen)
print("Area of Contours", area)
print("Arc_Length of Contours", arc_length)

cv2.imshow("Image", imgStacked)
cv2.waitKey(0)

