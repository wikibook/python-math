import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 데이터를 읽는다
dat = pd.read_csv('kimbab.csv', encoding='UTF-8')

print('사장님---------')
print('평균:', np.mean(dat['사장님']))
print('분산:', np.var(dat['사장님']))
print('표준편차:', np.std(dat['사장님']))

print('철수---------')
print('평균:', np.mean(dat['철수']))
print('분산:', np.var(dat['철수']))
print('표준편차:', np.std(dat['철수']))
