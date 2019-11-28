import math
import numpy as np

# 좌표
a = np.array([2, 7])
b = np.array([6, 1])
c = np.array([2, 3])
d = np.array([6, 5])

# 벡터a와 벡터b의 성분
va = b - a
vb = d - c

# 벡터의 크기
norm_a = np.linalg.norm(va)
norm_b = np.linalg.norm(vb)

# 벡터의 내적
dot_ab = np.dot(va, vb)

# 각도 구하기
cos_th = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_th)
deg = math.degrees(rad)
print(deg)
