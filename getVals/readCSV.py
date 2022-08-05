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
rcsvh = open('rData_H.csv')
bcsvh = open('bData_H.csv')
gcsvh = open('gData_H.csv')

rcsvl = open('rData-L.csv')
bcsvl = open('bData-L.csv')
gcsvl = open('gData-L.csv')


# read the csv data gathered for each channel

# high range values
csvReadRedh = csv.reader(rcsvh)
csvReadBlueh = csv.reader(bcsvh)
csvReadGreenh = csv.reader(gcsvh)
# low range values
csvReadRedl = csv.reader(rcsvl)
csvReadBluel = csv.reader(bcsvl)
csvReadGreenl = csv.reader(gcsvl)

# store the data as a list

# high
rdatah = list(csvReadRedh)
bdatah = list(csvReadBlueh)
gdatah = list(csvReadGreenh)
# low
rdatal = list(csvReadRedl)
bdatal = list(csvReadBluel)
gdatal = list(csvReadGreenl)


# remove the list of list format from the data
# high
rlisth = remLoL(rdatah)
glisth = remLoL(gdatah)
blisth = remLoL(bdatah)
# low
rlistl = remLoL(rdatal)
glistl = remLoL(gdatal)
blistl = remLoL(bdatal)

# convert numerical values from a string to integers
# high
rvalsh = lst_strToint(rlisth)
bvalsh = lst_strToint(blisth)
gvalsh = lst_strToint(glisth)
# low
rvalsl = lst_strToint(rlistl)
bvalsl = lst_strToint(blistl)
gvalsl = lst_strToint(glistl)


# get the size of the list for averaging
# high
rlenh = len(rvalsh)
blenh = len(bvalsh)
glenh = len(gvalsh)
# low
rlenl = len(rvalsl)
blenl = len(bvalsl)
glenl = len(gvalsl)

# get the new threshold value by averaging the data
# high
rthresh_h = int(rgbAv(rvalsh, rlenh))
bthresh_h = int(rgbAv(bvalsh, blenh))
gthresh_h = int(rgbAv(gvalsh, glenh))
# low
rthresh_l = int(rgbAv(rvalsl, rlenl))
bthresh_l = int(rgbAv(bvalsl, blenl))
gthresh_l = int(rgbAv(gvalsl, glenl))
# high
print("High Red threshold:", rthresh_h)
print("High Blue threshold:", bthresh_h)
print("High Green threshold:", gthresh_h)
# low
print("Low Red threshold:", rthresh_l)
print("Low Blue threshold:", bthresh_l)
print("Low Green threshold:", gthresh_l)

# print("The size of this array is:", rsize)

# rsize = len(rdata)
# gsize = len(gdata)
# bsize = len(bdata)

# print(rsize, gsize, bsize)


print(rvalsh)
print(gvalsh)
print(bvalsh)

print(rvalsl)
print(gvalsl)
print(bvalsl)



rmath = sum(rvalsh)
print(rmath)