import cv2
import argparse
import numpy as np
import time

def identifiers(videoFile, currentCascade, fileCounter):

	face_cascade = cv2.CascadeClassifier(currentCascade)

	"""
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
	"""
	cap = cv2.VideoCapture(videoFile)

	run_Cascade(face_cascade, cap, fileCounter)



def run_Cascade(face_cascade, cap, fileCounter):

	frameCount = 0
	count = 0


	while cap.isOpened():

		ret, img = cap.read()
		frameCount += 1
		#print frameCount
		if img is None:
			break


		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			if frameCount == 10:
				frameCount = 0
				cv2.imwrite("Frames/%d/frame%d.jpg" % (fileCounter, count), img)
				count += 1


		cv2.imshow('Captue', img)
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break



	cap.release()

	cv2.destroyAllWindows()

#identifiers()
