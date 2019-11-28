import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 기온 데이터를 읽는다
dat= pd.read_csv('temperature.csv', encoding='UTF-8')
n = len(dat)       # 데이터 수
x = range(1, n+1)  # x축값（1～데이터 수）

# 기온
y = dat['평균기온']  # y축값（평균기온）
plt.plot(x, y)       # 그래프를 그린다

# 구간 수를 9로 지정한 이동 평균
v = np.ones(9)/9.0
print(v)
y2 = np.convolve(y, v, mode='same')
plt.plot(x[4:n-4], y2[4:n-4])
plt.show()
