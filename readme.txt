## This file has the instructions ##

# Use case problem statement



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
    - UseCase
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
1. Change the directory to /mnt/c/Assignments/UseCase/
2. python main.py


# Logging details
1. Logging Configurations are stores in logging.json file. 
2. This has the error and info log files specified
3. The logs are stored/appended in info.log
4. The errors are added/appended in error.log