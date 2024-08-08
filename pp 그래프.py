import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

# df.describe().to_csv('./results/pima_describe.csv')

corr = df.corr(method='pearson')

df.hist(figsize=(12, 10), bins=5)
plt.tight_layout()
plt.show()