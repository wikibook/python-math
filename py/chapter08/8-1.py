import matplotlib.pyplot as plt
import pandas as pd

# salary.csv를 읽는다
dat = pd.read_csv('salary.csv', encoding='UTF-8')

# 데이터를 설정한다
x = dat['나이']
y = dat['연봉']

# 그래프를 그린다
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()
