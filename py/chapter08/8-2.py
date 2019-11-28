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

# 데이터의 개수
cnt = len(dat)

# 차분을 구한다
diff_y = []
for i in range(0, cnt-1):
    diff_y.append(y[i+1] - y[i])

# 그래프를 그린다
plt.plot(x[1:], diff_y)
plt.grid(color='0.8')
plt.show()
