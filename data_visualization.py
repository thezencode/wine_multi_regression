import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def quality_frequency(red_wine):
    sns.set(style="ticks", color_codes=True)
    sns.countplot(red_wine['quality'])

    plt.tight_layout()


def quality_pair_plot(red_wine, attributes):
    sns.set(style="ticks", color_codes=True)
    sns.pairplot(data=red_wine, vars=attributes, height=1, diag_kind='kde',
                 aspect=2)

    plt.tight_layout()


def quality_vs_acids(red_wine):
    sns.set(style="ticks", color_codes=True)
    sns.pairplot(data=red_wine, vars=['quality', 'fixed acidity', 'volatile acidity', 'citric acid', 'sulphates'],
                 height=1,
                 aspect=2)

    plt.tight_layout()


def quality_vs_sulfur_dioxides(red_wine):
    sns.set(style="ticks", color_codes=True)
    sns.pairplot(data=red_wine, vars=['quality', 'total sulfur dioxide', 'free sulfur dioxide'], height=1, aspect=2)

    plt.tight_layout()


def hist_of_all_attributes(red_wine, fig_size, num_bins):
    red_wine.hist(bins=50, figsize=fig_size)
    plt.tight_layout()