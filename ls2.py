import numpy as np
import cv2 as cv

img = cv.imread(r"C:\Users\Reto\Desktop\pythonProject\1.jpg", cv.IMREAD_COLOR)

# cv.line(img, [20,40], [60, 80], (255, 50, 0), 5)
# cv.rectangle(img, [60,80], [120,180], (255, 90, 30), 4)
# cv.circle(img, [120,180], 40, (200,90,90), 3)
# points = np.array([[20, 45], [50, 55], [60, 65], [80, 95], [100, 150], [150,20]], np.int32)
# cv.polylines(img, [points], False, (1200,10,5) )

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "reza torabi.",(20,300), font, 2, (255, 2, ), 3, cv.LINE_AA)






cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()