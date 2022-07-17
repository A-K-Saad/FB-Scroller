import cv2
import numpy as np
import pyautogui

cam = cv2.VideoCapture(0)
img_counter = 0
lower_black = np.array([22, 93, 0])
upper_black = np.array([45, 255, 255])
prev_y=0

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_black, upper_black)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
               pyautogui.press("space")

    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
