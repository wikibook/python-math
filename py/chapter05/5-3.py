import numpy as np
import matplotlib.pyplot as plt

# 사각형 ABCD의 정점
p = np.matrix([[3, 3, 5, 5, 3], [3, 1, 1, 3, 3]])

# 변환행렬(반시계 방향으로 45도 회전)
th = np.radians(45)     # 도수법 -> 호도법
A = np.matrix([[np.cos(th), np.sin(-th)], [np.sin(th), np.cos(th)]])

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
