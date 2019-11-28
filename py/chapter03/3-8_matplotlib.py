import matplotlib.pyplot as plt
import numpy as np

# 원의 중심
a = 200
b = 300

# 원의 방정식
r = 300                             # 반지름
x = np.arange(a-r, a+r+1)           # x값
y = np.sqrt(r**2 - (x-a)**2) + b    # y: 원의 위쪽
y2 = -y + 2 * b                       # y2: 원의 아래쪽

# 그리기
plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
