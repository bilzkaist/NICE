#*****************************************************************************
#
#                                      NIST Code.
#                             Written  by Bilal Dastagir.
#                                Sept, 07th, 2022
#
#******************************************************************************

# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.measure import shannon_entropy
import random 
import math
from PIL import Image 
import time
from itertools import combinations
from itertools import permutations
import statistics as st
from array import array
from skimage.filters.rank import entropy as en
from skimage.morphology import disk
#import imutiimls 
import os
from datetime import datetime



#Global Variables 
BETA = [0]
ALPHA = [1]
BRAVO  = [2]
CHARLIE = [3]

absolute_path = os.path.abspath(__file__)
#DIRPATH ="P:/workspace/vscode/python/VIMNFT" #os.path.dirname(absolute_path)
DIRPATH = os.path.normpath("P:/workspace/vscode/python/VIMNFT")

def get_image_paths(imagename):
    """
    function to combine directory path with individual image paths
    """
    abs_path = os.path.abspath(__file__)
    dirname = os.path.dirname(abs_path)
    #print("Full path: " + abs_path)
    #print("Directory Path: " +  dirname)
    fullpath = os.path.join(dirname, imagename)
    #print("Full path: " + fullpath)
    return fullpath


def getImageMark(originalImagePath="images/Bilal", dn=1):
    # Write code Here
    imageReadPath = get_image_paths(originalImagePath+""+".png")
    image = Image.open(imageReadPath)
    image.show()
    image_array = np.array(image)
    imageGray = image.convert('L')
    #imageGray.show()
    imageGrayResize = imageGray.resize((int(imageGray.width / dn), int(imageGray.height / dn)))
    image_array_resize = np.array(imageGrayResize)
    imageAlpha = image.convert("RGBA") # sets alpha to 255
    image_array_Mark = np.array(imageAlpha)
    #print("Image Shape : ", image_array_Mark.shape)
    a = image_array.shape[2]
    #print("a = ",a)
    timeNowStringFull = "Time : " +" "+ (datetime.now()).strftime("%H:%M:%S")+", " + datetime.today().strftime("%B %d, %Y")
    #print("Currently  : ",timeNowStringFull)
    timeNowString = str(datetime.now())
    #print("-> TS Str : ",timeNowString)
    timeNowNumpy = bytearray(timeNowString, encoding='utf8') #[elem.encode("hex") for elem in timeNowString]#np.zeros((100), dtype='datetime64[s]')
    #timeNowNumpy = np.fromstring(timeNowString, dtype=int, sep='')#np.array(map(int, timeNowString)) #np.array(list(timeNowString, dtype=int))
    
    #print("-> TS Np  : ",timeNowNumpy)

    #print("Currently  : ",timeNowString)
    timeNumpySize = len(timeNowString)
    #print("Time Numpy Size : ",timeNumpySize)
    #print("Time Now Numpy : ",timeNowNumpy)
    print("Created TimeStamp ................................. Time : ",timeNowNumpy)
    image_array_Mark[1][0][a] = int(timeNumpySize)
    for t in range(timeNumpySize): 
        #print(timeNowNumpy[t])
        image_array_Mark[0][t][a] = timeNowNumpy[t]
    # for i in range(image_array.shape[0]):
    #      for j in range(image_array.shape[1]):
    #         try: 
    #             if(j<timeNumpySize):
    #                 #print(timeNowNumpy[j])
    #                 #print("Before : ",image_array_Mark[i][j][a])
    #                 image_array_Mark[i][j][a] = timeNowNumpy[j]
    #                 #print("After : ",image_array_Mark[i][j][a])
    #             else:
    #                 image_array_Mark[i][j][a] = image_array_Mark[i][j][a]#image_array_resize[i][j]
    #         except:
    #             image_array_Mark[i][j][a] = image_array_Mark[i][j][a]#image_array_resize[i][j]
    
    imageMarked=Image.fromarray(image_array_Mark)
    imageMarkSavePath = get_image_paths(originalImagePath+"TimeStamped"+".png")
    imageMarked.save(imageMarkSavePath)
    return imageMarked

def isImageMark(originalImagePath="images/Bilal", dn=1):
    # Write code Here
    imageReadPath = get_image_paths(originalImagePath+""+".png")
    imageMarkReadPath = get_image_paths(originalImagePath+""+".png")
    image = Image.open(imageReadPath)
    imageMark = Image.open(imageMarkReadPath)
    image_array_Mark = np.array(imageMark)
    image_array = np.array(image)
    imageGray = image.convert('L')
    imageGrayResize = imageGray.resize((int(imageGray.width / dn), int(imageGray.height / dn)))
    image_array_resize = np.array(imageGrayResize)
    matchNumber = 0
    totalNumber = 0
    try:
        a = image_array.shape[2]
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]): 
                if (image_array_Mark[i][j][a-1] == image_array_resize[i][j]):
                    matchNumber = matchNumber+1

                totalNumber = totalNumber +1
        if (matchNumber==totalNumber):
            print("Image is Marked Properly!!!")
            print("Marking Ratio : ", int(matchNumber/totalNumber))
            return True
        else: 
            print("Image is Not Marked Properly !!!")
            print("Marking Ratio : ", int(matchNumber/totalNumber))
            return False
    except:
        print("Scalar Image Error: Image is Not Marked Properly !!!")
        print("Marking Ratio : ", int(0))
        return False

def getImageTimeStamp(originalImagePath="images/Bilal", timeNumpySize=26):
    # Write code Here
    imageReadPath = get_image_paths(originalImagePath+""+".png")
    image = Image.open(imageReadPath)
    image_array = np.array(image)
    a = int(image_array.shape[2] -1)
    #print("a = ",a)
    timeNowString = str(datetime.now())
    #print("-> TS Str : ",timeNowString)
    timeNowNumpy = bytearray(timeNowString, encoding='utf8') 
    #print("-> TS Np  : ",timeNowNumpy)
    error = 0
    #print("Currently  : ",timeNowString)
    #print("Time Numpy Size : ",len(timeNowString))
    #timeNumpySize = image_array[0][0][a]
    #print("Time Numpy Size  Retreived: ",timeNumpySize)
    #print("Time Now Numpy : ",timeNowNumpy)
    timeNumpyArray = timeNowNumpy#np.empty(timeNumpySize, dtype='int')
    print("Now TimeStamp ..................................... Time : ",timeNumpyArray)
    for i in range(timeNumpySize): 
        #print(timeNowNumpy[t])
        #timeNumpyArray[i] = image_array[0][i][a]
        try:
            #print(image_array[0][i][a])
            timeNumpyArray[i] = image_array[0][i][a]
        except:
            print("Error at t = ",i)
        
    # for i in range(image_array.shape[0]):
    #     for j in range(image_array.shape[1]):
    #         try: 
    #             if(j<timeNumpySize):
    #                 #print(timeNowNumpy[j])
    #                 #print("Before : ",image_array_Mark[i][j][a])
    #                 timeNumpyArray[j] = image_array[i][j][a]
    #                 #print("After : ",image_array_Mark[i][j][a])
    #             #else:
    #                 #timeNumpyArray[j] = 255#image_array_Mark[i][j][a]
    #                 #image_array_Mark[i][j][a] = image_array_Mark[i][j][a]#image_array_resize[i][j]
    #         except:
    #             error = error +1 
    #             #timeNumpyArray[j] = 255
    #             #print("Error Arrise !!!")
    #             #image_array_Mark[i][j][a] = image_array_Mark[i][j][a]#image_array_resize[i][j]
    print("Recovered TimeStamp ............................... Time : ",timeNumpyArray)


def run_beta(originalImagePath="images/Bilal", markImagePath="images/BilalMarked.png"):
    print("Beta Program is Started........... !!!")
    # Write code Here
    imageName = "images/lionfamily"
    imageNameMark = "images/lionfamilyTimeStamped"
    getImageMark(imageName).show()
    #isImageMark(imageNameMark)
    getImageTimeStamp(imageNameMark)

    print("Beta Program is Ended Successfully !!!")
    return BETA

def run_alpha():
    print("Alpha Program is Started........... !!!")
    # Write code Here
    print("Alpha Program is Ended Successfully !!!")
    return ALPHA
    

def run_bravo():
    print("Bravo Program is Started........... !!!")
    # Write code Here
    print("Bravo Program is Ended Successfully !!!")
    return BRAVO

def run_charlie():
    print("Charlie Program is Started........... !!!")
    # Write code Here
    print("Charlie Program is Ended Successfully !!!")
    return CHARLIE
    
def switch_mode(mode):
    # Program Started
    switcher = {
        0: run_beta,
        1: run_alpha,
        2: run_bravo,
        3: run_charlie
        
        
    }
     # Get the function from switcher dictionary
    func = switcher.get(mode, lambda: "Invalid mode")
    # Execute the function
    print("Mode Selected : ",func())
    # Program Ended 

def run():
    print("......................Main Program is Started........... !!!\n")
    # write coode here
    runMode = BETA
    if (runMode == ALPHA):
        run_alpha()
    else:
        run_beta()
        
    print("\n......................Main Program is Ended Successfully !!!")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_bye(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(' Bilal Dastagir')
    run()
    print_bye('Bilal Dastagir')