import cv2
import numpy as np
import os, os.path
import argparse
import detect

#Cascades to loop through
desiredCascades = ['cascade.xml', 'cascade_SittingMan2.xml', 'cascade_SittingMan3.xml', 'cascade_SittingMan4.xml']
#Holds the numbers of shapes in each video
numberOfShapesInEach = []

#Call the  cascades and gets the frames that have the object we are looking for
def callDetect(videoFile):
    fileCounter = 1
    for i in desiredCascades:
        print i
        detect.identifiers(videoFile, i, fileCounter)
        fileCounter += 1
        print "dead"

#callDetect()

#fins the "square in each of the frames"
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

#Calls our square menthos and puts the number of shapes in a list
def find_Squares_Files():
    #fileCounter = 1
    numberOfShapes = []
    i = 0
    index = 1

    while index < 5:

        path = ("Frames/%d" % index)
        file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        print file_count
        while i < file_count:

            numberOfShapes.append(find_Squares("Frames/%d/frame%d.jpg" % (index, i)))
            i += 1

        index += 1
        i = 0
        numberOfShapesInEach.append(numberOfShapes)

#find_Squares_Files()
#print numberOfShapesInEach

#counts the number of shapes in the video

def count_Shapes():
    print "-----------------------------------------"
    sum = 0
    for i in numberOfShapesInEach:
        for j in i:
            sum += j

    print sum
    return sum

#count_Shapes()
