import cv2

# cap  = cv2.VideoCapture("./images/cubase.mp4")
cap  = cv2.VideoCapture(1) # 获取摄像头

while True:

    ret, frame = cap.read()  # 返回两个值,下一帧是否获取成功和下一帧
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.8, fy=0.8)
        cv2.imshow("video", frame)
    else:
        break

    if cv2.waitKey(10) == ord('q'):  # 在屏幕上显示的时间1
        break

