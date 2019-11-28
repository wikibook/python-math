import matplotlib.pyplot as plt

# 데이터
x = list(range(1,11))           # x의 값（1～10）
y = []
for i in range(10):
    y.append(3 * x[i] - 24)     # y = 3x - 24

# 그래프
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()
