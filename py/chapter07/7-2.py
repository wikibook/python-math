import pandas as pd
import numpy as np

# score.csv를 읽는다
dat = pd.read_csv('score.csv', encoding='UTF-8')

# 평균값, 중앙값
print('평균값', np.mean(dat['수학']))
print('중앙값', np.median(dat['수학']))

# 최빈값
bincnt = np.bincount(dat['수학'])     # 같은 값의 개수를 센다
mode = np.argmax(bincnt)             # bincnt에 있는 값 중에 가장 큰 값을 꺼낸다
print('최빈치', mode)
