import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 6)    # x값
y = 1/2 * x + 1/2       # 직선1
y2 = -2 * x + 7     # 직선1에 직교하는 직선

# 그래프를 그린다
plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
