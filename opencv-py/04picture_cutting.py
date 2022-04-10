import cv2
import numpy as np
import random

img  = cv2.imread("./images/hl.jpg")

new_img = img[:150,200:400]
# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow("img", img)
cv2.imshow("newImg", new_img)

cv2.waitKey(0)  # 在屏幕上显示的时间
