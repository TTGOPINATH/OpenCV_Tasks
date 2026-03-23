import cv2
import numpy as np

img = cv2.imread("biscutts.jpeg")

crop = img[250:620, 180:680]

gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (5,5), 0)

_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0

for c in contours:
    if cv2.contourArea(c) > 200: 
        count += 1
        cv2.drawContours(crop, [c], -1, (0,255,0), 2)

print("Biscuits:", count)

cv2.imshow("Thresh", thresh)
cv2.imshow("Result", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()