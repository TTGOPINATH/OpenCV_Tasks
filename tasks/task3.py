import cv2
import numpy as nps
while True:
 image = cv2.imread('shapes.jpeg', 0)
 _,threshold = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
 contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 min_points = int(input("Enter the minimum number of points: "))
# draw the counters in continuous mode get the input in continuous mode and draw the contours.
 for contour in contours:
    aprox = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    if len(aprox) == min_points:
        cv2.drawContours(image, [aprox], 0, (0, 255, 0), 5)
    else:
        print("The shape has more than {} points".format(min_points))
 cv2.namedWindow('Shapes', cv2.WINDOW_NORMAL)
 cv2.imshow('Shapes', image)
#cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)
#cv2.imshow('Threshold', threshold)
 cv2.waitKey(0)
 cv2.destroyAllWindows()