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
    test_file_path = data_path + "test.csv"
    train_file_path = data_path + "train.csv"
    
    test_file = pd.read_csv(test_file_path, index_col=0)
    train_file = pd.read_csv(train_file_path, index_col=0)
    submission_file = pd.read_csv(submission_file_path, index_col=0)

if __name__ == "__main__":
    xgb_analysis()