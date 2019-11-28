import random

# 주사위를 던진다
hist = [0] * 7
for i in range(10000):
    dice = random.randint(1, 6)
    hist[dice] += 1

# 확률을 구한다
p = [0] * 7
for i in range(1, 7):
    p[i] = hist[i] / 10000
    print(i, p[i])

# 확률을 계산한다
print('------------------\n' + str(sum(p)))
