import matplotlib.pyplot as plt
import numpy as np

# 데이터
x = np.arange(-1.0, 1.01, 0.01)
y = 3 * x  # 일차함수

# 그래프를 그린다
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()
