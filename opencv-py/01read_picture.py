import cv2

img  = cv2.imread("./images/hdxzd.jpg")

# img  = cv2.resize(img,(400,500)) # 设置大小的方法

img  = cv2.resize(img,(0,0),fx=3.5,fy=3.5) # 另一种设置大小的方法

cv2.imshow("img",img)

cv2.waitKey(0) # 在屏幕上显示的时间