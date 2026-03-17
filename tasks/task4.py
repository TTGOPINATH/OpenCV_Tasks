import cv2
import numpy as np
image = cv2.imread('shapes.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
# Draw the counters for all the shapes in the image.
_,threshold = cv2.threshold(blur, 229, 255, cv2.THRESH_BINARY)
contours, hierarchies = cv2.findContours(
    threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
blank = np.zeros(threshold.shape[:2],  dtype='uint8')
cv2.drawContours(blank, contours, -1, (255, 0, 0), 1)
for i in contours:
    M = cv2.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
        cv2.circle(image, (cx, cy), 7, (0, 0, 255), -1)
        cv2.putText(image, "center", (cx - 20, cy - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.namedWindow('Contours',cv2.WINDOW_NORMAL)
cv2.imshow("Contours", blank)
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.imshow("Image",image)
cv2.imwrite("Image.jpeg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()