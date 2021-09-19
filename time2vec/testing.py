import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__=='__main__':
    columns = ['id', 'datetime', 'concept']
    train_df = pd.read_csv("../example_data/medical_training_data.csv", header=None, names=columns)
    med_df = pd.read_csv("../example_data/medical.csv")
    train_df['concept'].plot()
    plt.savefig('foo.png')