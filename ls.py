import cv2 as cv
from matplotlib import pyplot as plt

# img = cv.imread(r"C:\Users\Reto\Desktop\pythonProject\1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread(r"C:\Users\Reto\Desktop\pythonProject\2.jpg", 1)
# img3 = cv.imread(r"C:\Users\Reto\Desktop\pythonProject\2.jpg", -1)

# cv.imshow('gray', img)
# cv.imshow('color', img2)
# cv.imshow('org', img3)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv.imwrite(r"C:\Users\Reto\Desktop\pythonProject\gray.jpg", img)


plt.imshow(img2, interpolation='bicubic')
plt.plot([200,40],[40,80], 'c', linewidth=5)
# plt.xticks([]), plt.yticks([])
plt.show()

