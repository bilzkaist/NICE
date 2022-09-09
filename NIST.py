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


def markingImage():

def run_beta():
    print("Beta Program is Started........... !!!")
    # Write code Here
    dn = 1
    imageReadPath = get_image_paths("images/Bilal.png")
    image = Image.open(imageReadPath)
    image.show()
    imageGray = image.convert('L')
    #imageGray.show()
    imageGraySavePath = get_image_paths("images/BilalGray.png")
    imageGray.save(imageGraySavePath)
    imageGrayResize = imageGray.resize((int(imageGray.width / dn), int(imageGray.height / dn)))
    #imageGrayResize.show()
    imageGrayResizeSavePath = get_image_paths("images/BilalGrayResize.png")
    imageGrayResize.save(imageGrayResizeSavePath)
    image_array_resize = np.array(imageGrayResize)
    image_array = np.array(image)
    imageAlpha = image.convert("RGBA") # sets alpha to 255
    image_array_Mark = np.array(imageAlpha)
    #image_array_Mark = np.zeros((int(imageGray.height / dn), int(imageGray.width / dn),3)) #numpy.zeros((800, 800))
    print("Image Marked   : ", image_array_Mark.shape)
    print("Image Basic    : ", image_array.shape)
    print("Image Sized    : ", image_array_resize.shape)
    print("Image Length   : ", len(image_array))
    print("Image Shape[0] : ", image_array.shape[0])
    print("Image Shape[1] : ", image_array.shape[1])
    print("Image Shape[2] : ", image_array.shape[2])

    
    for i in range(image_array.shape[0]):
         for j in range(image_array.shape[1]):
            image_array_Mark[i][j][image_array.shape[2]] = image_array_resize[i][j]
            #for k in range(image_array.shape[2]):
             #   image_array_Mark[i][j][k] = image_array[i][j][k]
            #print("image_array[",i,"][",j,"][",[image_array.shape[2]-1],"]",image_array[i][j][image_array.shape[2]-1]) 
    # for i in range(image_array_resize.shape[0]):
    #      for j in range(image_array_resize.shape[1]):
    #         image_array_Mark[i][j][4] = image_array_resize[i][j]       
    #         for k in range(image_array.shape[2]):
    #             print("image_array[",i,"][",j,"][",k,"]",image_array[i][j][k]) 
    imageMarked=Image.fromarray(image_array_Mark)
    imageMarkSavePath = get_image_paths("images/BilalMarked.png")
    imageMarked.save(imageMarkSavePath)
    #imageMarked.show()
    imageMarkedReadPath = get_image_paths("images/BilalMarked.png")
    imageMarkedLoaded = Image.open(imageMarkedReadPath)
    imageMarkedLoaded.show()
    imageMarkedLoadedArray = np.array(imageMarkedLoaded)
    print("Image Marked Loaded   : ", imageMarkedLoadedArray.shape)
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