import matplotlib.pyplot as plt
import pandas as pd

# 데이터를 읽는다
dat = pd.read_csv('kimbab.csv', encoding='UTF-8')

# 도수분포표
plt.hist(dat['사장님'], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat['철수'], bins=range(0, 200, 10), alpha=0.5)
plt.show()
