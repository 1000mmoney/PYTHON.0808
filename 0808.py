import pandas as pd

colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

df.describe().to_csv('./results/pima_describe.csv')