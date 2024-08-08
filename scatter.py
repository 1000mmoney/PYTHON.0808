import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pandas.plotting import scatter_matrix

colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

# df.describe().to_csv('./results/pima_describe.csv')

scatter_matrix(df)
# pd.plotting.scatter_matrix(df)

plt.savefig("./results/scatterplot.png")
plt.show()
