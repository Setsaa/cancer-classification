#
# https://medium.com/analytics-vidhya/how-to-start-your-very-first-lung-cancer-detection-project-using-python-part-1-3ab490964aae
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from glob import glob

from sklearn.model_selection import train_test_split
from sklearn import metrics

import cv2
import gc
import os

import tensorflow as tf
from tensorflow import keras
from keras import layers

import warnings
warnings.filterwarnings('ignore')

path = 'LungImage_pyfile/'
classes = {
    0, 'benign',
    1, 'malignant'
}

IMG_SIZE = 28
SPLIT = 0.2
EPOCHS = 10
BATCH_SIZE = 64



X = []
Y = []

