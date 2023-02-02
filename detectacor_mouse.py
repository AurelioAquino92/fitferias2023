import cv2 as cv
import numpy as np

def click(event, x, y, flags, params):
    global frame, limMin, limMax
    if event == cv.EVENT_LBUTTONUP:
        frameHSV = cv.cvtColor(frame[y:y+1, x:x+1], cv.COLOR_BGR2HSV)
        for i in range(3):
            if limMax[i] < frameHSV[0, 0, i]:
                limMax[i] = frameHSV[0, 0, i]
            if limMin[i] > frameHSV[0, 0, i]:
                limMin[i] = frameHSV[0, 0, i]
        print(limMin, limMax)
        print((x, y))

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
limMin = [180, 255, 255]
limMax = [0, 0, 0]

cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0)
cap.set(cv.CAP_PROP_EXPOSURE, -5)

while True:
    _, frame = cap.read()
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(
        frameHSV,
        np.array(limMin, dtype=np.uint8),
        np.array(limMax, dtype=np.uint8)
    )
    cv.imshow('bgr', frame)
    cv.setMouseCallback('bgr', click)
    cv.imshow('res', cv.bitwise_and(frame, cv.cvtColor(mask, cv.COLOR_GRAY2BGR)))

    tecla = cv.waitKey(1)
    if tecla == ord('q'):
        break
    elif tecla == ord('z'):
        limMax = [0, 0, 0]
        limMin = [180, 255, 255]
