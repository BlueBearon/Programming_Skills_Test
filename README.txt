Author: Chase Packer

CSCI 435 - Software Engineering

Programming Skills Test

Purpose - This code takes pairs of an xml file and a png of its corresponding gui and then parses the xml file to find the bounds of the leaf elements of the gui and creates a new image
with all the gui elements highlighted with a yellow outline.


Libraries Required:

PIL (Pillow) - For Image Processing

Directions to Run:

Navigate to location of the python file "guiStructureFinder.py" in command line.

If necessary, install necessary libraries by running "pip install -r requirements.txt"

Run "python guiStructureFinder.py"

Resulting png files will be located in "GUI_Images" folder.

"Natural Language" Explanation:

This code is written in python as for a smaller project such as this, it was easier to use 
the libraries and quickly write the code without unnecessary complexity.  The code has been divided 
into several helper functions in order to make it clear what code does what and to divide concerns to 
make the code more readable and easier to understand.  The "main" function controls the main function of the code, 
selecting the file pairs and starting the process for each pair.  The "generateGui" function contains the overall
logic for extracting and parsing the xml data for files, as well as taking the bounding information
and drawing the yellow rectangle around each element.  It does this by calling helper functions
including: "prepareTree" (parses the tree and return the root element), "getLeaves" (Navigates the tree, 
finds the leaf nodes, and records the bounding information), "preparePng" (opens the image and 
creates a drawing object), "drawBounds" (Takes the bounding information from "getLeaves" and draws 
the yellow rectangles), and saveImg (Saves the modified image in special folder for review).

In order to make sure that this code could work with other xml/png file pairs in the future,
I decided to create code to navigate and retrieve the file names instead of hardcoding the filenames
into the code.





