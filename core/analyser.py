import pandas as pd
import matplotlib.pyplot as plt

import os

def plot_pie_chart ( csv_path, number_of_rows, sep=';' ) :
    if not os.path.isfile ( csv_path ):
        raise Exception("Caminho não representa um arquivo")
    df = pd.read_csv ( csv_path, sep=sep, nrows=number_of_rows )
    plot = df.plot.pie(labels=df['word'], y='count', figsize=(5,5))
    plt.show()
