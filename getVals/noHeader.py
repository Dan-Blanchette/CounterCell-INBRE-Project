#! python3
# This program will loop through all CSV files in a directory and remove the header entries
import csv,os
from genericpath import exists

os.makedirs('headerRemoved', exist_ok=True)
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
            continue

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
