import cv2
import numpy as np

image = cv2.imread('biscutts.jpeg')
crop_image = image[100:620,70:680]
gray = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (11, 11), 0)
canny = cv2.Canny(blur, 50, 110, 9)
_,thresh = cv2.threshold(blur,124,200,cv2.THRESH_BINARY)
dilated = cv2.dilate(thresh, (5, 5), iterations=0)

(cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rgb = cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
cv2.imshow('gray',gray)
cv2.imshow('Dilated',dilated)
cv2.imshow('color',rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Counters in the image : ", len(cnt))