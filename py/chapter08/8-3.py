import matplotlib.pyplot as plt
import numpy as np

# x값
x = np.arange(-10, 10, 0.1)

# 본래의 함수
y = x**3 + 3*x**2 + 3*x + 1
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()

# 도함수
y2 = 3*x**2 + 6*x + 3
plt.plot(x, y2)
plt.grid(color='0.8')
plt.show()
