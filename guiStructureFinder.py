'''
Author: Chase Packer

CSCI 435 - Software Engineering

Programming Skills Test

Purpose - This code takes pairs of an xml file and a png of its corresponding gui and then parses the xml file to find the bounds of the leaf elements of the gui and creates a new image
with all the gui elements highlighted with a yellow background
'''

import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
from pathlib import Path


'''
This method attempts to parse the provided xml file and returns the root element if successful.

Returns root node of XML file or 0 if parse fails
'''
def prepareTree(file):

    try:

        return ET.parse(file).getroot()
    except:

        print("File parse failed for " + file)
        return 0
    




'''
This method prepares the provided png to be copied and drawn on.

Returns the img file and the draw object
'''
def preparePng(file):

    with Image.open(file) as img:

        draw = ImageDraw.Draw(img)

    return img, draw


'''
This method finds all of the leaf nodes of the xml file using recursion. It also records the bounds of these nodes via the "getBounds" function
'''
def getLeaves(root, bounds):

    if len(root) == 0: #if there are no children, this is a leaf node
        str_bounds = root.get('bounds')
        getBounds(str_bounds, bounds)
    else:
        for child in root: #recursively find all of the leaf nodes
            getLeaves(child, bounds)

'''
This function formats records the bounds of a node (the str_bounds parameter) and puts it into the 2d bounds array

The node's bounds attribute starts off as a string with several unnecessary characters, so this function removes them,
and converts the string into an 4 element integer array with the correct bounds, then puts that into the 2d bounds array
'''
def getBounds(str_bounds, bounds):

    #Remove all '[' ']' ','
    str_bounds = str_bounds.replace('[', ' ')
    str_bounds = str_bounds.replace(']', ' ')
    str_bounds = str_bounds.replace(',', ' ')

    #Convert String to array
    num_bounds = str_bounds.split()

    #Convert String numbers into integers
    arr_bounds = [int(i) for i in num_bounds]

    #add the new array to the bounds 2d array
    bounds.append(arr_bounds)

'''
This function takes all of the bounding information in the bounds 2d array and draws the outlines of all gui elements
'''
def drawBounds(img, bounds):

    for arr in bounds:
        img.rectangle([(arr[0], arr[1]), (arr[2], arr[3])], outline = "yellow", width = 10)


'''
This function takes the provided edited image and saves it in the GUI_Images result folder
'''
def saveImg(img, name):

    filename = "GUI_Images/" + name[55:-4] + "gui.png" #remove ".png" and replace with "~gui.png"
    
    img.save(filename)


'''
This function contains the code for the process of parsing the xml tree and generating the gui image with the yellow outlines around the gui elements
'''
def generateGui(xml, png):

    bounds = []#2d array that will record all of the bounds for the nodes ie [[x11, y11, x12, y12], [x21, y21, x22, y22], ..., [xn1, yn1, xn2, yn2]]

    root = prepareTree(xml)#Parse the xml file and get the root node of the xml tree

    if(root != 0):

        getLeaves(root, bounds)#Get the bounds of the leaf nodes

        img, draw = preparePng(png)

        drawBounds(draw, bounds)#Draw the yellow outlines on all of the gui elements

        saveImg(img, png)

        print(png + " successful")


'''
This function reads through all the elements of the path folder and records the names of all the xml files (the png file should have the same name),
and then calls the generateGui function on all of them
'''
def main():


    filenames = []

    path = "Programming-Assignment-Data\Programming-Assignment-Data"
    mypath = Path(path)

    for item in mypath.iterdir():
    
        if item.is_file() and item.name[-4:] == ".xml":
            filenames.append(item.name[:-4])

    #call generateGui with the xml files and png files
    for fl in filenames:
        generateGui(path + "/" + fl + ".xml", path + "/" + fl + ".png")


if __name__ == "__main__":
    main()


