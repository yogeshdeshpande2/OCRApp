import cv2
import pytesseract
import os
from pytesseract import Output
import numpy as np
import matplotlib.pyplot as plt
from pathlib import (Path, PurePosixPath)
import yaml
import json

def load_configuration(path: str = "."):
    '''This function loads the config.yml file.'''
    conf = yaml.load(open(f'{path}/config.yml'), Loader=yaml.FullLoader)
    return conf


def load_logging_configuration(path: str = "."):
    '''This function loads the logging congfigurations'''
    with open(f'{path}/logging.json') as logging_json:
        logging_config = json.load(logging_json)
    return logging_config

def get_grayscale(img):
    """
    This function gets the grayscale image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                     


def thresholding(img):
    """
    This function gets the thresholding for the image
    """
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]   
    


def remove_noise(img):
    """
    This function remove noise
    """
    # Apply dilation and erosion to remove some noise  

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return cv2.GaussianBlur(img, (1,1), 0)


def ocr_main(img):
    """
    This function read the text from the image
    """
    custom_config = r'--oem 3 --psm 6'
    #return pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 6')
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config=custom_config, lang='eng')
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #cv2.imshow('img', img)
    #cv2.waitKey(0)
    #plt.rcParams['figure.figsize'] = [80, 80]
    #plt.imshow(img)
    #plt.show()
    
    parse_text = []
    word_list = []
    dict1 = {}

    last_word = ''
    last_word2 = ''
    companytype = ''
    companyname = ''
    status=''
    statusflag = 1
    companynameflag = 1
    nationalityflag=1
    companyperiod=''
    finyearendflag=1

    for word in d['text']:
        if word!='':
            
            #print(f"last_word2 -> {last_word2} & last_word -> [{last_word}] & word -> {word}")

            if (last_word == 'Status') or (nationalityflag == 0):
                if last_word == 'Status':
                    nationalityflag = 0
                
                if word != 'Nationality':
                    status = status + ' ' + word
                else:
                    nationalityflag = 1
                    dict1['Status'] = status

            elif (last_word2 == 'Company' and  last_word == 'Period') or (finyearendflag == 0):
                if (last_word2 == 'Company' and  last_word == 'Period'):
                    finyearendflag = 0
                
                if word != 'Financial':
                    companyperiod = companyperiod + ' ' + word
                else:
                    finyearendflag = 1
                    dict1['Company Period'] = companyperiod

            elif ((last_word2 == 'CR' and  last_word == 'No.') or (last_word2 == 'Registration' and  last_word == 'Date') or (last_word2 == 'Expiry' and  last_word == 'Date')):
                dict1[last_word2 + ' ' + last_word] = word
            
            elif last_word == 'Nationality' or last_word == 'CRNo.':
                dict1[last_word] = word
            
            elif (last_word2 == 'Year' and  last_word == 'End'):
                dict1['Financial Year End'] = word
            
            elif (last_word2 == 'Company' and  last_word == 'Type') or (statusflag == 0):
                if (last_word2 == 'Company' and  last_word == 'Type'):
                    statusflag = 0
                
                if word != 'Status':
                    companytype = companytype + ' ' + word
                else:
                    statusflag = 1
                    dict1['Company Type'] = companytype
            
            elif (last_word == '(English)' or (companynameflag == 0)):
                if last_word == '(English)':
                    companynameflag = 0
                
                if word != '‘Company':
                    companyname = companyname + ' ' + word
                else:
                    companynameflag = 1
                    dict1['Company Name'] = companyname
                
            word_list.append(word)
            last_word2 = last_word
            last_word = word

            if (last_word!='' and word == '') or (word==d['text'][-1]):
                parse_text.append(word_list)
                word_list = []
            
            exit
    
    return(dict1)
    