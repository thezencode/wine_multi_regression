import pandas as pd
import requests


def wine_data():

    url_1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    url_2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    r_1 = requests.get(url_1)
    r_2 = requests.get(url_2)
    red_location = '/home/thezencode/PycharmProjects/wine_analysis/wine_multi_regression/winequality-red.csv'
    white_location = '/home/thezencode/PycharmProjects/wine_analysis/wine_multi_regression/winequality-white.csv'

    with open(red_location, 'wb') as f:
        f.write(r_1.content)

    with open(white_location, 'wb') as g:
        g.write(r_2.content)

    red_quality = pd.read_csv(red_location, delimiter=';')
    white_quality = pd.read_csv(white_location, delimiter=';')

    return red_quality, white_quality

