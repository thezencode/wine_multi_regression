import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from import_wine_data import wine_data
from zlib import crc32
from sklearn.model_selection import train_test_split

from data_visualization import quality_frequency, quality_pair_plot, quality_vs_acids, \
    quality_vs_sulfur_dioxides, quality_vs_sulfur_dioxides, hist_of_all_attributes

red_wine, white_wine = wine_data()

# this returns two pandas DataFrame objects


print(red_wine.info())
print(red_wine.describe())

# Basic info and description for our data set

# combining and playing around attributes
# red_wine["General Acidity"] = red_wine['citric acid'] + red_wine['fixed acidity']

train_set, test_set = train_test_split(red_wine, test_size=0.2, random_state=42)

# Check correlations
corr_matrix_red = red_wine.corr()
print(corr_matrix_red['quality'].sort_values(ascending=False))

# Top 4 attributes in terms of correlations
attributes = ['quality', 'alcohol', 'sulphates', 'citric acid', 'fixed acidity']

# reverting to a clean data set
 

