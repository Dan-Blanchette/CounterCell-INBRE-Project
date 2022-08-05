import cv2
import numpy as np
import os
import csv 

click = cv2.EVENT_LBUTTONDOWN

# Logic for bitmask
# image[:,:,2] == redthresh & image[:,:,1] == greentresh & image[:,: 0] == bluethresh

def getRed(event, x, y):
    # open file called bData.csv and have it append clicked entries to a file
    rFile = open("rData_H.csv", "a", newline='')
    rOutput = csv.writer(rFile)
    # if the user left clicks, store all red values to a .csv file
    if event == click:
        rColor = image[y, x, 2]
        # list.append(rColor)
        # print(list)
    
        rOutput.writerow([str(rColor)])
        # cast numpy value as a str and print to .csv file
        rFile.close()
         
        print("Red: ", rColor)

    return rColor

def getBlue(event, x, y):
    # open file called bData.csv and have it append clicked entries to a file
    bFile = open("bData_H.csv", "a", newline='')
    bOutput = csv.writer(bFile)
    # if the user left clicks, store all blue values to a .csv file
    if event == click:
        bColor = image[y, x, 0]
        bOutput.writerow([str(bColor)])
        bFile.close()
        print("Blue:" , bColor )
    return bColor
        

def getGreen(event, x, y):
    # open file called bData.csv and have it append clicked entries to a file
    gFile = open("gData_H.csv", "a", newline='')
    gOutput = csv.writer(gFile)
    # if the user left clicks, store all green values to a .csv file
    if event == click:
        gColor = image[y, x, 1]
        gOutput.writerow([str(gColor)])
        gFile.close()
        print("Green: ", gColor)
    return gColor


def getRGB_click(event, x, y, flags, param, counter = 0):
    # check if left mouse button is depressed
    if event == click:
        # get and print R, G, and B values
        rValue = getRed(event,x,y)
        gValue = getGreen(event, x, y)
        bValue = getBlue(event, x, y)
        # print the BGR tuple as  (BGR is the order of channels for the CV2 modude)
        # colors = image[y, x]
    
        print("RGB Format: ", rValue, gValue, bValue)
        print("Coordinates of pixel: X: ", x, "Y: ", y, "\n")

# Read an image, create a window and bind the function to the window
image = cv2.imread("../pngimgs/1.png")
cv2.namedWindow('mouseRGB', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('mouseRGB', getRGB_click)
# before the while loop, if there are any .csv files
# clear the contents of each file for writing
# else continue with program.
for csvFile in os.listdir('.'):
    if csvFile.endswith('_H.csv'):
        f = open(csvFile, 'r+')
        f.truncate(0)
    else:
        continue

# run until the escape key is pressed
while(1):
    cv2.imshow('mouseRGB', image)
    if cv2.waitKey(20) & 0xFF == 27:
        #os.remove("bData.csv")
        #os.remove("gData.csv")
        #os.remove("rData.csv")
        break
# if escape is pressed finish.
cv2.destroyAllWindows()