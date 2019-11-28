import matplotlib.pyplot as plt
import numpy as np

# 각도
th = np.arange(0, 360)

# 원주 위에 있는 점 P의 좌표
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

# 그리기
plt.plot(x, y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
