import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

# df.describe().to_csv('./results/pima_describe.csv')
plt.clf()
corr = df.corr(method='pearson')

df.hist(figsize=(12, 10), bins=5)
plt.tight_layout()

df.plot(kind='box', subplots=True, figsize=(12, 10), layout=(3, 3), sharex=False, sharey=False)
# plt.savefig("./results/hitplot.png")
# df.plot(kind='density', subplots=True, figsize=(12, 10), layout=(3, 3), sharex=False)

plt.show()


