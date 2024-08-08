import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

# df.describe().to_csv('./results/pima_describe.csv')
df.plot(kind='density', figsize=(12, 10), subplots=True, layout=(3, 3), sharex=False)
plt.savefig("./results/densityplot.png")
