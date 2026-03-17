import cv2
import numpy as nps
image = cv2.imread('shapes.jpeg', 0)
_,threshold = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
min_points = int(input("Enter the minimum number of points: "))
for contour in contours:
    aprox = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    x = aprox.ravel()[0]
    y = aprox.ravel()[1]
    
    if len(aprox) >= min_points:
        if len(aprox) == 3:
            cv2.drawContours(image, [aprox], -1, (0,255,0), 3)
            #cv2.putText(image, 'Rectangle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            #print(len(aprox))
    elif len(aprox) == 4:
        cv2.drawContours(image, [aprox], -1, (255,0,0), 3)
        #cv2.putText(image, 'Triangle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
        #print(len(aprox))
    elif len(aprox) == 7:
        cv2.drawContours(image, [aprox], -1, (0,0,255), 3)
        #cv2.putText(image, 'Circle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        #print(len(aprox))
    else:
        cv2.drawContours(image, [aprox], -1, (0,255,255), 3)
            #cv2.putText(image, 'Other', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 2)
            #print(len(aprox))

#cv2.namedWindow('Shapes', cv2.WINDOW_NORMAL)
cv2.imshow('Shapes', image)
#cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)
#cv2.imshow('Threshold', threshold)
cv2.waitKey(0)