import cv2

img_grey = cv2.imread('images/yamaguchi', 0)
cv2.imwrite('images/sample3.jpg', img_grey)
