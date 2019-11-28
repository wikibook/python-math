import matplotlib.pyplot as plt
import pandas as pd

# 데이터를 읽는다
dat = pd.read_csv('score.csv', encoding='UTF-8')

# 산포도
plt.scatter(dat['수학'], dat['과학'])
plt.axis('equal')
plt.show()
