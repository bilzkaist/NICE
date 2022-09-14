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

def get_image_paths(imagename):
    """
    function to combine directory path with individual image paths
    """
    abs_path = os.path.abspath(__file__)
    dirname = os.path.dirname(abs_path)
    fullpath = os.path.join(dirname, imagename)
    return fullpath

def makeNFTImageMark():
    # Write code Here
    return 0


def extractNFTImageMark():
    # Write code Here
    return 0

def run_beta(originalImagePath="images/Bilal", markImagePath="images/BilalMarked.png"):
    print("Beta Program is Started........... !!!")
    # Write code Here
    imageName = "images/lionfamily"
    imageNameMark = "images/lionfamilyTimeStamped"

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
        