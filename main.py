#import save_model

import tensorflow as tf
import subprocess
from absl import app, flags, logging
from absl.flags import FLAGS
from core.yolov4 import YOLO, decode, filter_boxes
import core.utils as utils
from core.config import cfg

import os, platform, subprocess, re

from save_model_build import save_tf

# comment out below line to enable tensorflow logging outputs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time
import tensorflow as tf
import tensorflow.keras as keras


physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
from absl import app, flags, logging
from absl.flags import FLAGS
import core.utils as utils
from core.yolov4 import filter_boxes
from tensorflow.python.saved_model import tag_constants
from core.config import cfg
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
# deep sort imports
from deep_sort import preprocessing, nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker
from tools import generate_detections as gdet

def get_CPU_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    return ""

def get_GPU_name():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        print("Current GPU:")
        print("Name:", gpu.name, "  Type:", gpu.device_type)
     
    
    
global GPU, CPU




# MODULE 1: EVOKE CONSOLE, GET PARAMETERS
    # CALL ON SAVE_MODEL, Load model

# MODULE 2: GET NECESSITIES
# 1. Input path  
# 2. Output path
#Module 1 and 2 can be in main file

# MODULE 3: GET OPTIONS
# INPUT_FPS
# OUTPUT_FORMAT
# YOLOV4-TINY?
# FRAMEWORK: Tensorflow (tf), trt, TensorflowLite (tflite)
# MODEL: Yolov3 or Yolo v3
# IOU Threshold (default 0.45)
# Score: confidence threshold (default 0.55)
# Dont_show: dont show video output
# Info?: print detailed info about tracked objects

#Module 3 should be in one file, tracker_options.py
#should return an array of tuple in this format ((tiny, True), (input_fps, 60), ...)

# MODULE 4: Evoke track.py with all necessities and options

# MODULE 5: Return

# Module 6: Rerun yolov4?
#   Yes: Different parameter?
#       Yes: Go back to module 1
#       No: Different video?
#           Yes: Go to module 2
#           No: rerun Module 6

# Module 7: Out

def main(_argv):
    loop = True
    CPU = get_CPU_name()
    GPU = get_GPU_name()
    while(loop):
        #Documentation
    
        #Module 1 
        exec(open('object_tracker.py').read())
    
        #Module 2
        output_path = input()
        input_path = input()
    
        #Module 3
        options = ['--video ./data/video/test.mp4','--output ./outputs/demo.avi','--model yolov4']
        
        #Module 4
        parameters = ['object_tracker.py']
        for i in options:
            parameters.append(options[i])
        subprocess.call(parameters)
        
        #Module 5
        
        #Module 6
        if loop is False:
            break
        else:
            continue
    
    
    
    
    
    
    

    
if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass