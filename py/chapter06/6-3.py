import matplotlib.pyplot as plt
import random
import math

# 점을 그린다
cnt = 0
for i in range(3000):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    d = math.sqrt((x-50)**2 + (y-50)**2) #중심과 점 사이의 거리
    if (d <= 50 ):
        cnt += 1   # 원 안에 있는 점을 센다
        plt.scatter(x, y, marker='.', c='r')  # 빨간색 점을 그린다
    else:
        plt.scatter(x, y, marker='.', c='g')  # 초록색 점을 그린다
plt.axis('equal')
plt.show()

# 원주율을 구한다
p = cnt / 3000  # 점이 원 안에 있을 확률
pi = p * 4      # 원주율
print(pi)
