import numpy as np
import matplotlib.pyplot as plt

# 삼각형 ABC의 정점
p = np.matrix([[1, 1, 2, 1], [3, 1, 1, 3]])

# 변환행렬(3배로 확대)
A = np.matrix([[3, 0], [0, 3]])

# 변환
p2 = A * p
print(p2)

# 그리기
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
