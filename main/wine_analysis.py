import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from import_wine_data import wine_data
from zlib import crc32
from sklearn.model_selection import train_test_split
from heatmap import heatmap as hp
from heatmap import corrplot as cp

from data_visualization import quality_frequency, quality_pair_plot, quality_vs_acids, \
    quality_vs_sulfur_dioxides, quality_vs_sulfur_dioxides, hist_of_all_attributes

red_wine, white_wine = wine_data()

# this returns two pandas DataFrame objects


print(red_wine.info())
print(red_wine.describe())

# Basic info and description for our data set

train_set, test_set = train_test_split(red_wine, test_size=0.2, random_state=42)

# Graphical visualization
#####################################################

# Check correlations
# corr_matrix_red = red_wine.corr()
# print(corr_matrix_red['quality'].sort_values(ascending=False))

# plot correlations
# plt.figure(figsize=(8, 8))
# cp(data=corr_matrix_red, size_scale=300)
# plt.save-fig('wine_data_corr_plot.png')

# plot pair-plot of attributes that have a positive correlation with the the quality of wine

# quality_pair_plot(red_wine, ['quality', 'alcohol', 'sulphates', 'citric acid', 'fixed acidity'])
###################################################




 

