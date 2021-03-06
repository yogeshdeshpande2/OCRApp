import sys
from datetime import datetime
import os
import time
import json
import logging.config
import logging

from utils import get_grayscale, thresholding, remove_noise, ocr_main, load_configuration, load_logging_configuration
import cv2
import pytesseract
from skimage.filters import threshold_local
import numpy as np
import opencv_wrapper as cvw

path = os.getenv("ETL_FRAMEWORK_HOME", ".")




def action_main(_config, logger_main):
    '''This is a starting point where based on action triggered, respective operation will be performed'''
    oks = []
    noks = []
    print("====================")
    print("== Processing action ==")
    print("====================") 

    # Read the config parameters
    _source_base = _config['ocr']['source_base']
    _source_image_path = _config['ocr']['source_image_path']
    _target_text_path = _config['ocr']['target_text_path']
    
    # Logs the parameters in case of debugging
    logger_main.info(f"=== Config parameters ===")
    logger_main.info(f"_source_base -> {_source_base}")
    logger_main.info(f"_source_image_path -> {_source_image_path}")
    logger_main.info(f"_target_text_path -> {_target_text_path}")

    # Traverse complete image folder to process all the images
    for folder, subfolder, files in os.walk(_source_image_path):
        for currentfile in files:

            fullimagepath = _source_image_path + currentfile
            logger_main.info(f"## Processing image : {fullimagepath} ##")

            # Reads the image
            image = cv2.imread(fullimagepath)
            (h, w) = image.shape[:2]
            image = cv2.resize(image, (w*3, h*3))

            # Get the grayscale image
            image = get_grayscale(image)

            # Remove the noise from the image
            image = remove_noise(image)

            # Get the grathresholding on the image
            image = thresholding(image)
            
            # Process the image to extract the text in key-value pairs i.e. dictionary form
            return_dict = ocr_main(image)

            # Build the target text file which will have the dictionary key-value pairs extracted
            target_file_path = _target_text_path + currentfile.rsplit('.', 1)[0] + '.txt'
            
            # Writes the dictionary values to the text file
            logger_main.info(f"Creating a text file {target_file_path} ...")
            with open(target_file_path, 'w') as convert_file:
                convert_file.write(json.dumps(return_dict))        


def execute_job():
    """
    This is the function where starts the program execution.
    """
    print("=============================================")
    print("== Use Case    ==")
    print("=============================================")

    # Load job configuration
    config = load_configuration(path)

    # Load logging configuration
    logging_config = load_logging_configuration(path)
    logging.config.dictConfig(logging_config)
    logger_main = logging.getLogger(__name__)

    # Python logging
    logger_main.info('Initializing...')
    
    start = time.time()
    
    action_main(
        config,
        logger_main
        )
        
    end = time.time()

    logger_main.info("===============")
    logger_main.info("== Use case Completed ==")
    logger_main.info("===============")
    
if __name__ == '__main__':
    execute_job()