import unittest
import yaml
import os
import logging.config
import logging
import json
from utils import load_configuration, load_logging_configuration

path = os.getenv("ETL_FRAMEWORK_HOME", ".")

class TestCap(unittest.TestCase):
    def test_one(self):
        '''
        This test checks text file is created for each image file 
        i.e. count of text files = count of images
        '''
        source_file_count = 0
        target_file_count = 0
        for folder, subfolder, files in os.walk(_source_image_path):
            for currentfile in files:
                    source_file_count += 1
        logger_main.info(f"_source_image_path File count -> {source_file_count}")

        for folder, subfolder, files in os.walk(_target_text_path):
            for currentfile in files:
                    target_file_count += 1
        logger_main.info(f"_source_image_path File count -> {target_file_count}")   
        self.assertEqual(target_file_count, source_file_count)

    
    def test_two(self):
        '''
        This test checks text file for each image file 
        i.e. image1.JPG should have text file as image1.txt
        If any mismtach, test fails and shows the file which is missing
        '''
        file_match_flag = True
        for folder, subfolder, files in os.walk(_source_image_path):
            for currentfile in files:
                if file_match_flag == True:
                    sourcefile1 = os.path.splitext(currentfile)[0]
                    logger_main.info(f"source file -> {currentfile}")

                    file_match_flag = os.path.isfile(_target_text_path + sourcefile1 + '.txt')
                    logger_main.info(f"target file -> {sourcefile1 + '.txt'}")

                    if file_match_flag != True:
                        logger_main.info(f"file_match_flag  -> {file_match_flag} on file {currentfile}")
                        exit

                
        self.assertEqual(file_match_flag, True)


if __name__ == '__main__':
    _config = load_configuration(path)

    # Load logging configuration
    logging_config = load_logging_configuration(path)
    logging.config.dictConfig(logging_config)
    logger_main = logging.getLogger(__name__)

    # Python logging
    logger_main.info('Initializing...')

    #Read the config parameters
    _source_base = _config['ocr']['source_base']
    _source_image_path = _config['ocr']['source_image_path']
    _target_text_path = _config['ocr']['target_text_path']

     # Logs the parameters in case of debugging
    logger_main.info(f"=== Config parameters ===")
    logger_main.info(f"_source_base -> {_source_base}")
    logger_main.info(f"_source_image_path -> {_source_image_path}")
    logger_main.info(f"_target_text_path -> {_target_text_path}")

    unittest.main()
