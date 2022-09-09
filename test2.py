from PIL import Image
import os

# get the directory path of the current python file
abs_path = os.path.abspath(__file__)
dirname = os.path.dirname(abs_path)
print("Full path: " + abs_path)
print("Directory Path: " +  dirname)
fullpath = os.path.join(dirname, "images/wall.jpeg")
print("Full path: " + fullpath)
image = Image.open(fullpath)
image.show()

