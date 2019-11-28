import matplotlib.pyplot as plt
import numpy as np

# x값
x = np.arange(-1, 1, 0.1)

# 본래의 함수
y = 2*x*x + 3

# 접선
a = 4*0.25            # 도함수  （기울기）
b = 3.125 - a * 0.25  # 절편
y2 = a*x + b          # 접선의 식

# 그래프를 그린다
plt.plot(x, y)   # 본래의 함수
plt.plot(x, y2)  # 접선
plt.grid(color='0.8')
plt.show()
