import matplotlib.pyplot as plt
import numpy as np

# 데이터
x = np.array([23,24,28,24,27,21,18,25,28,20])  # 기온
y = np.array([37,22,62,32,74,16,10,69,83,7])   # 쥬스의 판매량

# 회귀직선
a, b = np.polyfit(x, y, 1)
y2 = a * x + b
print('기울기: {0}, 절편:{1}'.format(a, b))    #기울기와 절편을 표시한다

# 그린다
plt.scatter(x, y)  # 산포도
plt.plot(x, y2)    # 회귀직선
plt.show()
