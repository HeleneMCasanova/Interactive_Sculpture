import cv2
import argparse
import numpy as np
import time
import Shapes
import os, shutil

def identifiers():

	face_cascade = cv2.CascadeClassifier("Cascades/cascade_SittingMan2.xml")


	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video", help="path to the video file")
	ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
	args = vars(ap.parse_args())

	# if the video argument is None, then we are reading from webcam
	if args.get("video", None) is None:
		cap = cv2.VideoCapture(0)
		time.sleep(0.25)
	# otherwise, we are reading from a video file
	else:
		cap = cv2.VideoCapture(args["video"])

	#cap = cv2.VideoCapture(videoFile)

	run_Cascade(face_cascade, cap)

def destroy_Files():
    folder = 'Frames/clips'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def run_Cascade(face_cascade, cap):

    frameCount = 0
    count = 0
    start_time = time.time()

    while cap.isOpened():

        ret, img = cap.read()
        frameCount += 1
        print frameCount
        if img is None:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            #print "Frame Count: ", frameCount

            if frameCount >= 10:
                frameCount = 0
                #print frameCount
                cv2.imwrite("Frames/clips/frame%d.jpg" % count, img)
                count += 1
                print "in"

        cv2.imshow('Captue', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

        current_time = time.time() - start_time
        print current_time
        if current_time >= 60:
            Shapes.find_Squares_Files()
            Shapes.count_Shapes()
            start_time = time.time()
            destroy_Files()
            count = 0
            Shapes.clear()
            print start_time

    cap.release()
    cv2.destroyAllWindows()

#identifiers()
