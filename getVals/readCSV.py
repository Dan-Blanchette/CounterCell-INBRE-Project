from email.contentmanager import raw_data_manager
import cv2
import os
import csv
import pandas as pd

rcsv = open('rData.csv')
bcsv = open('bData.csv')
gcsv = open('gData.csv')

csvReadRed = csv.reader(rcsv)
csvReadBlue = csv.reader(bcsv)
csvReadGreen = csv.reader(gcsv)

rdata = list(csvReadRed)
bdata = list(csvReadBlue)
gdata = list(csvReadGreen)

print(rdata)
print(gdata)
print(bdata)