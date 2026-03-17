import cv2
import numpy as np

image = cv2.imread('shapes.jpeg')
lower_blue = np.array([90, 50, 190])
upper_blue = np.array([94, 200, 255])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#lower_pink = np.array([0, 20, 150])
#upper_pink = np.array([20, 50, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#mask2 = cv2.inRange(hsv, lower_pink, upper_pink)
#mask = cv2.bitwise_or(mask, mask2)
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blue Shapes Mask', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image)
cv2.imshow('Blue Shapes Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()