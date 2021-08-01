# OCRApp

## This file has the instructions ##

# Use case problem statement
Test instructions:
1.Using following steps, fetch the required data
a. https://www.sijilat.bh/
b. In the homepage, choose “All”-> under public service section choose "Search Cr"
c. enter a company name of your choice or "HSBC"
d. click on the cr.no to open the form
e. save the screenshots as images, make sure that the Basic information and company information are present in one image
		(You need to have a minimum of 10 such images in a folder with the name "images" )

2.For each image file in the folder images, using openCV or Tesseract, extract content in the form of key-value pairs and write the key-value pairs to a file. For E.g.
 
For the above images, the key-value pairs will be in the form of {“Country”:”Bahrain”,”Status”:”Active”,”Registration Date”:”08/04/1961”,”Company Period”:”N/A”}

3. Zip all the images and the extracted key-value pairs along with the python code and send it to this mail id.
4. You have a max time of 2 days for this. If you are facing any problems please write back to this mail id
5. Please maintain appropriate coding guidelines to submit the assignment and you are free to use any open source Python package to achieve this
6. Validate your solution on more than on company and provide set-up instructions 
7. Optional tasks: Create a simple Web App where company name should be provided as an input and key-value pairs will be the output, Dockerize the solution and isolate the logic as Python package



# Solution Approach
   A] Configuration setup
     - Common parameters are defined in a config file
   B] Utils library
     - Common library functions are defined in this file
   C] main program
     - Program execution starts with main.py
     - Reads the parameters
     - Traverse through the images folder and process each image
     - For each image, extracts the data and text will be stored in its text file in key-value format
     - During processing, gets all the words from the image and then create key-value pairs as per image template


# Testing
   A] Unit test case 1 : Checks the count of source image files match with the target text files
   B] Unit test case 2 : Checks each source image file has its text file created


# Folder structure
    Assignments
    - OCRApp
        - images [source images will be stored at this path]
        - text   [target text files will be created at this path]
        config.yml
        error.log
        info.log
        Logging.json
        main.py
        utils.py
        test.py
        readme
        requirements.txt


# Setup/Installation
1. Install the required libraries
2. Create the folder structure and copy the files
3. Download and copy the images under the images subfolder


# How to run the program
1. Change the directory to /mnt/c/Assignments/OCRApp/
2. python main.py


# Logging details
1. Logging Configurations are stores in logging.json file. 
2. This has the error and info log files specified
3. The logs are stored/appended in info.log
4. The errors are added/appended in error.log