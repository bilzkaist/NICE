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
import os



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
    print("Full path: " + abs_path)
    print("Directory Path: " +  dirname)
    fullpath = os.path.join(dirname, imagename)
    print("Full path: " + fullpath)
    return fullpath


def run_beta():
    print("Beta Program is Started........... !!!")
    # Write code Here
    imageReadPath = get_image_paths("images/Bilal.png")
    image = Image.open(imageReadPath)
    image.show()
    image_array = np.array(image)
    print("Image Length : ", len(image_array))
    print("Image Shape[0] : ", image_array.shape[0])
    print("Image Shape[1] : ", image_array.shape[1])
    print("Image Shape[2] : ", image_array.shape[2])
    imageSavePath = get_image_paths("images/Bilal.png")
    image.save(imageSavePath)
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