#!/usr/bin/env python
import os
import math
import random

import xgboost
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xgboost_util


def print_performance(files, write_to_simulator=False):
    real = []
    predicted = []
    for f in files:
        data = xgboost_util.prepare_files([f], WINDOW_SIZE, scaling, TARGET_COLUMN)
        inputs, outputs = xgboost_util.make_io(data)

        y_pred = model.predict(xgboost.DMatrix(inputs, feature_names = data[0][0].columns))
        pred = y_pred.tolist()

        real += outputs
        predicted += pred

    xgboost_util.print_metrics(real, predicted)


def main(test_name):
    random.seed(0)

    NUMBER_OF_TREES = 50
    WINDOW_SIZE = 5

    TARGET_COLUMN = 'flow_size'

    TRAINING_PATH = '../data/ml/' + test_name + '/training/'
    TEST_PATH = '../data/ml/' + test_name + '/test/'
    VALIDATION_PATH = '../data/ml/' + test_name + '/validation/'

    training_files = [os.path.join(TRAINING_PATH, f) for f in os.listdir(TRAINING_PATH)]
    test_files = [os.path.join(TEST_PATH, f) for f in os.listdir(TEST_PATH)]
    validation_files = [os.path.join(VALIDATION_PATH, f) for f in os.listdir(VALIDATION_PATH)]

    scaling = xgboost_util.calculate_scaling(training_files)
    data = xgboost_util.prepare_files(training_files, WINDOW_SIZE, scaling, TARGET_COLUMN)

    inputs, outputs = xgboost_util.make_io(data)

    # fit model no training data
    param = {
        'num_epochs' : NUMBER_OF_TREES,
        'max_depth' : 10,
        'objective' : 'reg:linear',
        'booster' : 'gbtree',
        'base_score' : 2,
        'silent': 1,
        'eval_metric': 'mae'
    }

    training = xgboost.DMatrix(inputs, outputs, feature_names = data[0][0].columns)
    print len(outputs)
    print 'Training started'
    model = xgboost.train(param, training, param['num_epochs'])

    print 'TRAINING'
    print_performance(training_files)
    print

    print 'TEST'
    print_performance(test_files)
    print

    print 'VALIDATION'
    print_performance(validation_files)

if __name__ == "__main__":
    print("Starting running experiment:\n")
    for test_name in ["KMeans", "PageRank", "SGD", "tensorflow", "web_server"]:
        print(test_name)
        main(test_name)

