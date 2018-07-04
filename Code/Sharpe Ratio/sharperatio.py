# Author:           Sheldon Reddy
#
# Description:      This script accesses Yahoo Finance stream to obtain financial data
#                   The data is then used to perform the following:
#                                                                   1. Sharpe Ratio
#
# Dataset:          The dataset is sourced from https://www.kaggle.com/bindubalusu/stock-market
#                   The dataset contains basic stock parameters and is small which will be great for basic functionality
#

# Imports
import numpy as np
import pandas as pd
import seaborn as sb
import csv

# Read in data using Pandas CSV Reader
data = pd.read_csv('data.csv')

print(data.head())