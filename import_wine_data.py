import pandas as pd
import requests


def wine_data():

    url_1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    url_2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    r_1 = requests.get(url_1)
    r_2 = requests.get(url_2)

    with open("winequality-red.csv", 'wb') as f:
        f.write(r_1.content)

    with open("winequality-white.csv", 'wb') as g:
        g.write(r_2.content)

    red_quality = pd.read_csv("winequality-red.csv", delimiter=';')
    white_quality = pd.read_csv("winequality-white.csv", delimiter=';')

    return red_quality, white_quality

