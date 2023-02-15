import numpy as np
import cv2 as cv

img = cv.imread(r"C:\Users\Reto\Desktop\pythonProject\3.jpg", cv.IMREAD_COLOR)
# imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# imgCopy = img[100:120, 200:220]
# img[150:170, 250:270]= imgCopy
# cv.imshow('img', img)
# cv.imshow('imgGray', imgGray)
# cv.imshow('img2', img2)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
cv.imshow('Img', img)

cv.waitKey(0)
cv.destroyAllWindows()