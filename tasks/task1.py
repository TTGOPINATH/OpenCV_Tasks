import cv2
import numpy as np
image = cv2.imread('shapes.jpeg') 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([90, 50, 70])
upper_blue = np.array([128, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.namedWindow('Blue Shapes', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
cv2.imshow('Blue Shapes', image)
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()