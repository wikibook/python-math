import random

# 주사위를 던진다
cnt= 0  # 1이 나온 횟수
for i in range(10000):
    dice = random.randint(1, 6)
    if dice == 1:
        cnt += 1

# 확률을 구한다
p = cnt / 10000
print(p)
