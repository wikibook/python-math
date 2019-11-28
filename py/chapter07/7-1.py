import pandas as pd

# score.csv를 읽는다
dat = pd.read_csv('score.csv', encoding='UTF-8')
dat.head()     # 내용을 확인한다
