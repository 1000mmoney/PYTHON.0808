# matplotlib 설치
import matplotlib.pyplot as plt

#pandas 설치
import pandas as pd

# numpy 설치
import numpy as np

# scikit-learn 설치
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from sklearn.linear_model import LinearRegression

# 각 항목 이름 붙이기
colums = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=colums)

# 바꾸기 할 항목 범위 정하기
array = data.values
X = array[:, 0:8]
Y = array[:, 8]

# # 소수점 아래로 바꾸기 1 : 미니맥스스케일러
# scaler = MinMaxScaler(feature_range=(0, 1))
# rescaled_X = scaler.fit_transform(X)
# print(rescaled_X)
#
# # 소수점 아래로 바꾸기 2 : 스탠다드스케일러
# scaler = StandardScaler()
# rescaled_X = scaler.fit_transform(X)
# print(rescaled_X)
#
# # 0 또는 1의 값을 바꾸는 방법 : 바이너라이저
scaler = Binarizer(threshold=0.5)
rescaled_X = scaler.fit_transform(X)
# print(rescaled_X)


model = LinearRegression()
model.fit(X, Y)

predicted_Y = model.predict(X)
y = (predicted_Y > 0.5).astype(int)

print(y)