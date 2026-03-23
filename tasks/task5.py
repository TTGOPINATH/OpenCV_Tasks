import cv2
import numpy as np

img = cv2.imread("biscutts.jpeg")
crop = img[250:620,180:680]
hsv = cv2.cvtColor(crop,cv2.COLOR_BGR2HSV_FULL)
#color = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(hsv,(11,11),-1,cv2.BORDER_DEFAULT)
_,thresh = cv2.threshold(blur,170,255,cv2.THRESH_BINARY)
conv = cv2.cvtColor(thresh,cv2.COLOR_BGR2GRAY)
#_,thresh1 = cv2.threshold(conv,100,255,cv2.THRESH_BINARY)
croped = conv[200:600,50:640]
#cv2.imshow("Gray",color)
#cv2.imshow("Cropped",crop)
#cv2.imshow("HSV",hsv)
#cv2.imshow("Thresh1",thresh1)
cv2.imshow("Threshold",thresh)
#cv2.imshow('Converted',conv)
#cv2.imshow("cropped_image",croped)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print("Counters in the image : ", len(cnt))