import numpy as np
import matplotlib.pyplot as plt

# 삼각형 ABC의 정점
p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])

# 변환행렬(x축의 선대칭)
A = np.matrix([[1, 0], [0, -1]])

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
