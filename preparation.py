import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

# df.describe().to_csv('./results/pima_describe.csv')

corr = df.corr(method='pearson')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(colums)
ax.set_yticklabels(colums)

plt.show()

plt.savefig("./results/corrplot.png")