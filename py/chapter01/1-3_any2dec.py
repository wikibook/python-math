def any2dec(target, m):
    n = len(target)-1 	# 지수 최댓값
    sum = 0           	# 10진수로 변환한 값

    # 문자 수 만큼 반복한다
    for i in range(len(target)):
        if target[i] == 'A':    num = 10
        elif target[i] == 'B':  num = 11
        elif target[i] == 'C':  num = 12
        elif target[i] == 'D':  num = 13
        elif target[i] == 'E':  num = 14
        elif target[i] == 'F':  num = 15
        else:                   num = int(target[i])

        sum += (m ** n) * num       # “m의 n승 x 각 행의 값”의 합계를 낸다
        n -= 1                      # 무게를 한 개 줄인다
    return sum



# 2진수 ‘11010’을 10진수로 변환한다
print(any2dec('11010', 2))
# 16진수 ‘1A’를 10진수로 변환한다
print(any2dec('1A', 16))
