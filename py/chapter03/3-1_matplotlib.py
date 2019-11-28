import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5, 6, 7]
y = [64.3, 63.8, 63.6, 64.0, 63.5, 63.2, 63.1]

# 그래프를 그린다
plt.plot(x, y)        	# 꺾은선을 그린다
plt.grid(color='0.8') 	# 격자를 표시한다
plt.show()            	# 화면에 표시한다
