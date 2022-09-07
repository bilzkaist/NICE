from PIL import Image
import os

# get the directory path of the current python file
abs_path = os.path.abspath(__file__)
dirname = os.path.dirname(abs_path)
print("Full path: " + abs_path)
print("Directory Path: " +  dirname)
fullpath = os.path.join(dirname, "P:/workspace/vscode/python/VIMNFT/images/wall.jpg")
print("Full path: " + fullpath)
image = Image.open(fullpath)
image.show()
# im1 = Image.open(r'P:/workspace/vscode/python/VIMNFT/images/wall.jpg')
# im1.show()
# im1.save(r'P:/workspace/vscode/python/VIMNFT/images/wall.png')