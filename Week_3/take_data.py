import cv2
import os

video_capture = cv2.VideoCapture(0)
cframe=0


a=input(str("Enter the User Id: "))

if os.path.exists(a):
    print("Id already exists")
    
else: 
    os.makedirs(a)

    while (cframe<=50):
        success, frame = video_capture.read()
        cv2.imshow("Output", frame) 
        cv2.imwrite(a+'.jpg', frame)
        cframe +=1
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
video_capture.release() 
cv2.destroyAllWindows()