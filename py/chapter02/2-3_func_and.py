def func_and(score):
    if score >= 80:                         # socore가 80이상
        rank = 'A'
    elif (score >= 60) and (score < 80):    # score가 60～79의 범위 안에 있다
        rank = 'B'
    elif (score >= 40) and (score < 60):    # score가 40～59의 범위 안에 있다
        rank = 'C'
    else:                                   # 위에 있는 어떤 범위에도 들지 않는다(score가 40미만）
        rank = '추가 시험'
    return rank



rank = func_and(78)
print(rank)
