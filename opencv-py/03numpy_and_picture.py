import cv2
import numpy as np
import random

img  = cv2.imread("./images/hl.jpg")

for row in range(300):
    for col in range(img.shape[1]):
        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow("img", img)

cv2.waitKey(0)  # 在屏幕上显示的时间

################################################################################################
# img = np.empty((300,300,3),np.uint8)
#
# for row in range(300):
#     for col in range(300):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
#
# cv2.imshow("img",img)
#
# cv2.waitKey(0) # 在屏幕上显示的时间

#############################################################################
# print(img)
# print(type(img))
# print(img.shape)