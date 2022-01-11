# -*- coding: utf-8 -*-
"""
@time:2021/11/25 15:32
@Author:Yukino
"""

import cv2 as cv

def video_demo():
    capture = cv.VideoCapture(0);
    while True:
        ref, frame = capture.read()
        cv.imshow("Mask Recognize",frame)
        c = cv.waitKey(30) & 0xff
        if c == 27:
            capture.release()
            break

video_demo()
cv.waitKey()
cv.destroyAllWindows()


# import cv2
#
# face_cascade = cv2.CascadeClassifier(r"./haarcascade_frontalface_default.xml")
#
# faces = face_cascade.detectMultiScale(
#    gray,
#    scaleFactor = 1.15,
#    minNeighbors = 5,
#    minSize = (5,5),
#    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
# )

