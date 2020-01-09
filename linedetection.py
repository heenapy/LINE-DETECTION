import cv2
import numpy as np

# ___________________LINE DETECTION___________________

image = cv2.imread('su.png')
cv2.imshow('real',image)
print(image.shape)
print(len(image))
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,225,225,apertureSize=3)
lines = cv2.HoughLines(edges,1,np.pi /180,200)
print(lines)
# if lines is not None:
for a1 in lines:
    print(a1[0])
    rho, theta = a1[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a * rho
    y0 =b * rho
    x1=int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image,(x1,y1),(x2,y2),(0,0,250),2)
cv2.imshow('Hough lines',image)
cv2.waitKey()