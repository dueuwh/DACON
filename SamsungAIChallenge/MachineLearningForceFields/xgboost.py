import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
import itertools

def xgb_analysis():
    data_path = "./data/"
    submission_file_path = data_path + "sample_submission.csv"
    test_file_path = data_path + "Test.xyz"
    train_file_path = data_path + "Train.xyz"
    
    test_list = []
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            test_list.append(line)

    train_list = []
    with open(train_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            train_list.append(line.strip())
    
    submission_file = pd.read_csv(submission_file_path, index_col=0)

    print("test_list: ", test_list)

if __name__ == "__main__":
    xgb_analysis()