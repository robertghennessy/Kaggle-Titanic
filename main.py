import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    target_column = ['Survived']
    # load in the csv files
    test = pd.read_csv('data_files/test.csv')
    train = pd.read_csv('data_files/train.csv')
    # split the features from the target
    train_target = train[target_column]
    train_features = train.drop(target_column, axis=1)
    # create a dictionary to return the


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
