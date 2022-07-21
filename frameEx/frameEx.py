import cv2
import os
import pymediainfo as pinfo
from PIL import Image
"""
Author: Daniel Blanchette
Date: 6/29/2022

Copyright (c) 2002, Daniel Blanchette
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
"""

# gets frames per second from the video source
def fps(path):

    video = cv2.VideoCapture(path)

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second in the video: {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second the video: {0}".format(fps))

    video.release()

def count_frames_manual(video):
    #
    total=0

    while True:
        #
        (grabbed, frame) = video.read()

        if not grabbed:
            break

        total += 1
    #
    return total


# this function will get the frame count from a video
def count_frames(path, override=False):
    # grab a pointer to the video file and initialize the total
    # number of frames read
    video = cv2.VideoCapture(path)
    total = 0

    # if the override flag is passed in, revert to the manual
    # method for couting frames
    if override:
        total = count_frames_manual(video)

    #
    else:
        
        try:
            total = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        
        except:
            total = count_frames_manual(video)
    
    video.release()

    return total



""" 
 # extracts frames from the video file and converts them in to .png files
 - the user specifies the file path for the video to be converted
 - and the target directory for the files to be stored in. 

 # The function also calls fps() and count_frames() to provide the
 # user analysis on frames per second for the video and total frames processed
""" 
def frame_extractor(vidpath, dirpath):

    fileInfo = pinfo.MediaInfo.parse(vidpath)
    for track in fileInfo.tracks:
        if track.track_type == "Video":
            # variable that will contain the video capture from the specified file
            vidcap = cv2.VideoCapture(str(vidpath))  
    
    if (os.path.isdir(dirpath)) == 1:
        print("Directory already exists")
        exit(0)
    else:
        os.mkdir(dirpath)

    # send the images to the specified user directory
    path = dirpath

    # This function sets the time between frame captures
    # and names the extracted still image files
    def getFrame(sec):
        
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        hasFrames, image = vidcap.read()
        # if the file is a video file, export the frames as
        # image files named zeb and append the frame number and file type to the end of
        if hasFrames == 1:
            cv2.imwrite(os.path.join(path, str(count) + ".png"), image)
            return hasFrames

    # This block initializes variables and sets the specified frame rate to 0.5 seconds
    # What this block does is it takes the 19 second video and sections the image into
    # half second still images. The output for the 19 second video is 39 images.
    # this happens because the computer has to determine if there is still data to be processed
    # and if so create an additional image so it is not lost.
    sec = 0
    frameRate = 0.5
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    # Error checking to ensure program successfully extracted the frames
    if success != 0:
        dir = (os.getcwd() + "/" + path)
        print("The program has successfully completed!\n")
        print("Files have been exported to", str(dir))

