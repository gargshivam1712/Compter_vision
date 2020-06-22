import cv2
import numpy
import time

video = cv2.VideoCapture(0) 
while(True): 
	ret, frame = video.read() 
	cv2.imshow('Camera', frame) 
	if cv2.waitKey(1) & 0xFF == ord('q'):  # to quit the camera frame
		break
vid.release() 
cv2.destroyAllWindows() 
