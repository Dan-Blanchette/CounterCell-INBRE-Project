from email.contentmanager import raw_data_manager
import cv2
import os
import csv
import pandas as pd


# remove list of lists format to a list of strings
def remLoL(data):
    flat_list=[]
    for sublist in data:
        for item in sublist:
            flat_list.append(item)
    return flat_list

# convert the lists from str to int
def lst_strToint(data):
    new_list = []
    new_list = [int(i) for i in data]
    return new_list

# average the csv list data
def rgbAv(data, l):
    average = (sum(data) / l) 
    return int(average)

# read the csv data
rcsv = open('rData.csv')
bcsv = open('bData.csv')
gcsv = open('gData.csv')

# read the csv data gathered for each channel
csvReadRed = csv.reader(rcsv)
csvReadBlue = csv.reader(bcsv)
csvReadGreen = csv.reader(gcsv)

# store the data as a list
rdata = list(csvReadRed)
bdata = list(csvReadBlue)
gdata = list(csvReadGreen)

# remove the list of list format from the data
rlist = remLoL(rdata)
glist = remLoL(gdata)
blist = remLoL(bdata)

# convert numerical values from a string to integers
rvals = lst_strToint(rlist)

# get the size of the list for averaging
rlen = len(rvals)

# get the new threshold value by averaging the data
rthresh = int(rgbAv(rvals, rlen))

print("Red threshold:", rthresh)


# print("The size of this array is:", rsize)

# rsize = len(rdata)
# gsize = len(gdata)
# bsize = len(bdata)

# print(rsize, gsize, bsize)


print(rvals)
print(glist)
print(blist)

rmath = sum(rvals)
print(rmath)