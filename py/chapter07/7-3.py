import matplotlib.pyplot as plt
import pandas as pd

# score.csv를 읽는다
dat = pd.read_csv('score.csv', encoding='UTF-8')

# 각 계급에 포함되는 도수를 센다
hist = [0]*10 			# 도수(요소 수 10개를 0으로 초기화한다)
for dat in dat['수학']:
    if dat < 10:   hist[0] += 1
    elif dat < 20:  hist[1] += 1
    elif dat < 30:  hist[2] += 1
    elif dat < 40:  hist[3] += 1
    elif dat < 50:  hist[4] += 1
    elif dat < 60:  hist[5] += 1
    elif dat < 70:  hist[6] += 1
    elif dat < 80:  hist[7] += 1
    elif dat < 90:  hist[8] += 1
    elif dat <= 100:  hist[9] += 1
print('도수:', hist)

# 도수분포표
x = list(range(1,11))  # x축에 해당되는 값
labels = ['0~','10~','20~','30~','40~','50~','60~','70~','80~','90~']	# x축 눈금에 쓰는 레이블
plt.bar(x, hist, tick_label=labels, width=1)				# 막대그래프를 그린다
plt.show()
