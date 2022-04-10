import cv2
import numpy as np
# import random
kernel = np.ones((3,3),np.uint8)
kernel1 = np.ones((3,3),np.uint8)

img  = cv2.imread("./images/hl.jpg")

img  = cv2.resize(img,(0,0),fx=0.4,fy=0.4)
# 1)灰阶
GRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 把彩色图片变成灰阶
# 2)高斯模糊
blur = cv2.GaussianBlur(img,(15,15),10)
# 3)取边缘
canny = cv2.Canny(img,150,200)
# 4) 边缘膨胀
dileate = cv2.dilate(canny,kernel,iterations=1 )
# 5) 线条变细
erode  = cv2.erode(dileate,kernel1,iterations=1 )

# cv2.imshow("img", img)
# cv2.imshow("grey", GRAY)
# cv2.imshow("blur", blur)
# cv2.imshow("canny", canny)
cv2.imshow("dileate", dileate)
cv2.imshow("erode", erode)
cv2.waitKey(0)  # 在屏幕上显示的时间
