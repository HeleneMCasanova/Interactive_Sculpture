import cv2
import numpy as np
import os, os.path
import argparse
import casCall

#Holds the numbers of shapes in each video
numberOfShapesInEach = []

#Calls our main function to populate our clips file
def main():
    casCall.identifiers()

#main()

def clear():
    numberOfShapesInEach = []

def find_Squares(imagePath):
    numberOfShapes = 0

    image = cv2.imread(imagePath)

    lower = np.array([0, 0, 0])
    upper = np.array([15, 15, 15])
    shapeMask = cv2.inRange(image, lower, upper)
    # find the contours in the mask
    (cnts, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print "I found %d black shapes" % (len(cnts))
    #cv2.imshow("Mask", shapeMask)

    numberOfShapes = (len(cnts))
    print "The number of shapes: ", numberOfShapes

    cv2.waitKey(30)

    return numberOfShapes

#find_Squares()

def find_Squares_Files():
    #fileCounter = 1
    numberOfShapes = []
    i = 0


    path = ("Frames/clips")
    file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print file_count
    while i < file_count-1:

        numberOfShapes.append(find_Squares("Frames/clips/frame%d.jpg" % (i)))
        i += 1

    numberOfShapesInEach.append(numberOfShapes)

#find_Squares_Files()
#print numberOfShapesInEach

def count_Shapes():
    print "-----------------------------------------"
    sum = 0
    for i in numberOfShapesInEach:
        for j in i:
            sum += j

    print sum

    if sum <= 20000:
        print "desired"
    else:
        print "undesired"

#count_Shapes()
