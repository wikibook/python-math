import numpy as np
import matplotlib.pyplot as plt

# 삼각형 ABC의 정점(동차좌표)
p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1],[1, 1, 1, 1]])

# 변환행렬
A = np.matrix([[1, 0, 2], [0, 1, 3], [0, 0, 1]])  # 평행이동
th = np.radians(90)
B = np.matrix([[np.cos(th), np.sin(-th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])  # 회전행렬

# 변환
p2 = B * A * p  # 평행이동->회전
print(p2)

# 그리기
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
