'''
version: 0.1.12    
author: Jeffrey Jean-Pierre
license: MIT
'''

import string
from subprocess import PIPE, Popen
import sys
import traceback


dataproviderArray = []

def chompy(csvPathInput):
    # open the csv based on user input for file path
    print('opening csv')
    if (csvPathInput != None):
        csvPath = csvPathInput
    else:
        csvPath = str(raw_input('filename: '))
    csv = Popen('cat ' + str(csvPath), shell=True, stdout=PIPE)

    # then extract contents of the csv into an array
    print('extracting contents of csv')
    mydata = csv.communicate()[0][0:].split(',')

    # one time needed to run, but useful if you have the right data
    print('building codes object')
    cc = open('file-to-compare-second-dataset-to.csv', 'r')
    lines = [line.rstrip('\n') for line in cc]
    linesFromC = []
    for data in lines: linesFromC.append(data.split("\t"))
    results = {}
    for cLine in linesFromC: results[cLine[0]] = {'iso2': cLine[1], 'iso3': cLine[2]}

    # create the array from the csv we opened
    print('creating')
    newArray = []
    label = str(csvPath[0:-4])
    labelInCaps = string.capwords(label.replace("-", " "))
    try:
        # colors need fixing
        colors = {'a':"#D4DCDA", 'b':"#D1D79D", 'c':"#Db8e70",'d':"#8ED0DD",'e':"#DD7DDD"}

        # format the newArray of objects with names for your generated file by removing hyphens and capitalizing everything
        for d in mydata: newArray.append({'customData': labelInCaps, 'title': d, 'id': results[d]['iso2'], 'groupId': label, 'color': colors[label]}); dataproviderArray.append({'customData': labelInCaps, 'title': d, 'id': results[d]['iso2'], 'groupId': label, 'color': colors[label]})

        # new json to store stuff
        print('creating file')
        filename = label + '.json'
        jsonFile = open(filename, 'w+')
        jsonFile.write(str(newArray))
        jsonFile.close()
    except Exception:
        print(traceback.format_exc())

if __name__ == "__main__":
    try:
        arg1 = str(sys.argv[1])
        csvPathInput = str(arg1)
        chompy(csvPathInput)
    except:
        # if no argument is passed, will run for all in this list.
        # breaks if file is missing
        filenamesToPull = ['asia-and-the-pacific.csv', 'africa.csv', 'americas.csv', 'europe-and-central-asia.csv', 'arab-states.csv'] 
        for r in filenamesToPull:
            chompy(r)
    
        # create a new json file and store the array
        print('creating dataprovider areas array')
        filename = 'data-provider-areas' + '.json'
        jsonFile = open(filename, 'w+')
        jsonFile.write(str(dataproviderArray))
        jsonFile.close()