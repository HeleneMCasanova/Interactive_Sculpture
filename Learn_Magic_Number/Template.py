import cv2
import argparse
import numpy as np
import time

cascade = cv2.CascadeClassifier('cascade.xml')
cascade_one = cv2.CascadeClassifier('cascade_SittingMan2')

ap = argparse.ArgumentParser()
ap.add_argument("v", "--video", help = "path to video file")
ap.add_argument("a", "--min-area", type = int, default = 500, help = "minimum area size")
args = vars(ap.parse_args())

if args.get("video", None) is None:
    cap = cv2.VideoCapture(0)
    time.sleep(25)

else:
    cap = cv2.VideoCapture(args["video"])

while cap.isOpened():
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in body:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        body_one = cascade_one.detectMultiScale(roi_gray)
        for(ax,ay,aw,ah) in body_one:
            cv2.rectangle(img, (ax,ay), (ax+aw,ay+ah), (255,255,0), 2)

    cv2.imShow('Capture', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
