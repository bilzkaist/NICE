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


class NICE:
    def __init__(self):
        x=0

def getImagePaths(imagename):
    """
    function to combine directory path with individual image paths
    """
    abs_path = os.path.abspath(__file__)
    dirname = os.path.dirname(abs_path)
    fullpath = os.path.join(dirname, imagename)
    return fullpath

def makeNFTImageMark(originalImagePath="images/Bilal.png", messageString="Bilal Dastagir", dn=1):
    # Write code Here
    try:
        imageReadPath = getImagePaths(originalImagePath+".png")
    except:
        imageReadPath = getImagePaths(originalImagePath)
    imageOriginal = Image.open(imageReadPath)
    imageOriginal.show()
    imageOriginalArray = np.array(imageOriginal)
    imageOriginalGray = imageOriginal.convert('L')
    #imageOriginalGray.show()
    imageOriginalGrayArray = np.array(imageOriginalGray)
    imageMarkString = messageString + " with Time : " +" "+ (datetime.now()).strftime("%H:%M:%S")+", " + datetime.today().strftime("%B %d, %Y")
    print("Image Mark Message : ",imageMarkString)
    imageMarkNumpy = bytearray(imageMarkString, encoding='utf8')
    imageMarkNumpySize = len(imageMarkString)
    print("Image Mark Size : ", imageMarkNumpySize)
    imageMark = imageOriginal.convert("RGBA")
    #imageMark.show()
    imageMarkArray = np.array(imageMark)
    imageMarkArrayFinal = np.array(imageMark)
    a = imageMarkArray.shape[2] - 1
    imageMarkArray[1][0][a] = imageMarkNumpySize 
    print("Created TimeStamp .................................  ",imageMarkNumpy)
    for i in range(imageMarkArray[1][0][a]):
        imageMarkArray[0][i][a] = imageMarkNumpy[i]
    
    imageMarked = Image.fromarray(imageMarkArray)
    imageMarked.show()

    imageMarkedSavePath = getImagePaths(originalImagePath+"Stamped"+".png")
    imageMarked.save(imageMarkedSavePath)
    
    # for i in range(imageOriginalArray.shape[0]):
    #     for j in range(imageOriginalArray.shape[1]):
    #         for k in range(imageOriginalArray.shape[2]):
    #             imageMarkArray[i][j][k] = 255- imageMarkArray[i][j][k] 
    # imageMarked = Image.fromarray(imageMarkArray)
    # imageMarked.show()
    # imageMarkedGray = imageMarked.convert('L')
    # imageMarkedGray.show()
    # imageMarkedGrayArray = np.array(imageMarkedGray)
    # for x in range(imageOriginalArray.shape[0]):
    #     for y in range(imageOriginalArray.shape[1]):
    #         if (imageMarkedGrayArray[x][y]>225):
    #             imageMarkedGrayArray[x][y] = 0
    #             imageMarkArrayFinal[x][y][0] = 0
    #             imageMarkArrayFinal[x][y][1] = 0
    #             imageMarkArrayFinal[x][y][2] = 0
    #         elif (imageMarkedGrayArray[x][y]<25):
    #             imageMarkedGrayArray[x][y] = 255
    #             imageMarkArrayFinal[x][y][0] = 255
    #             imageMarkArrayFinal[x][y][1] = 255
    #             imageMarkArrayFinal[x][y][2] = 255
    #         else:
    #             imageMarkedGrayArray[x][y] = 255
    #             #imageMarkArrayFinal[x][y][0] = 255
    #             #imageMarkArrayFinal[x][y][1] = 255
    #             #imageMarkArrayFinal[x][y][2] = 255
    # imageGrayMarked = Image.fromarray(imageMarkedGrayArray)
    # imageGrayMarked.show()
    # imageMarkedFinal = Image.fromarray(imageMarkArrayFinal)
    # imageMarkedFinal.show()
    # imageDifferenceArray = np.array(imageOriginal)
    # for i in range(imageOriginalArray.shape[0]):
    #     for j in range(imageOriginalArray.shape[1]):
    #         for k in range(imageOriginalArray.shape[2]):
    #             if (imageMarkArrayFinal[i][j][k] == imageOriginalArray[i][j][k]):
    #                 imageDifferenceArray[i][j][k] = 255
    # imageDifference = Image.fromarray(imageDifferenceArray)
    # imageDifference.show()

    return imageMarked


def extractNFTImageMark(markedImagePath="images/BilalStamped.png", messageString="Bilal Dastagir", dn=1):
    # Write code Here
    try:
        imageReadPath = getImagePaths(markedImagePath+".png")
    except:
        imageReadPath = getImagePaths(markedImagePath)
    imageMarked  = Image.open(imageReadPath)
    imageMarked.show()
    imageMarkString = messageString + " with Time : " +" "+ (datetime.now()).strftime("%H:%M:%S")+", " + datetime.today().strftime("%B %d, %Y")
    #print("Image Mark Message : ",imageMarkString)
    imageMarkNumpy = bytearray(imageMarkString, encoding='utf8')
    print("Currently TimeStamp .................................  ",imageMarkNumpy)
    imageMarkedArray = np.array(imageMarked)
    a = imageMarkedArray.shape[2] - 1
    imageMarkedNumpySize = imageMarkedArray[1][0][a] 
    for i in range(imageMarkedNumpySize):
        imageMarkNumpy[i] = imageMarkedArray[0][i][a]
    print("Extracted TimeStamp .................................  ",imageMarkNumpy)
    
    return 0

def run_beta(originalImagePath="images/Bilal", markImagePath="images/BilalMarked.png"):
    print("Beta Program is Started........... !!!")
    # Write code Here
    imageName = "images/Bilal"
    imageNameMark = "images/lionfamilyStamped"
    #imageMarked = makeNFTImageMark(imageName)
    extractNFTImageMark(imageNameMark)

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
        