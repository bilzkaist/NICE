#*****************************************************************************
#
#                                      NIST Code.
#                             Written  by Bilal Dastagir.
#                                Sept, 07th, 2022
#
#******************************************************************************

from PIL import Image
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
    image_names = []
    print("Print->", os.path.join(dirname, imagename))
    fullpath = os.path.join(DIRPATH, imagename)
    #fullpath = (dirname+imagename)
    print("Full path: " + fullpath)
    image_names.append(fullpath)
    return image_names


def run_beta():
    print("Beta Program is Started........... !!!")
    # Write code Here
    imageReadPath = "P:/workspace/vscode/python/VIMNFT/images/Bilal.jpg"
    imageSavePath = "P:/workspace/vscode/python/VIMNFT/images/Bilal.png"
    im1 = Image.open(r"P:/workspace/vscode/python/VIMNFT/images/Bilal.jpg")
    im1.show()
    im1.save(r"P:/workspace/vscode/python/VIMNFT/images/Bilal.png")
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