import cv2

img  = cv2.imread("./images/hdxzd.jpg") # 读入内存,用变量img存储

# img  = cv2.resize(img,(400,500)) # 绝对大小

img  = cv2.resize(img,(0,0),fx=3.5,fy=3.5) # 相对大小

cv2.imshow("img",img)

cv2.waitKey(0) # 在屏幕上显示的时间
