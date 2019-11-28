def dec2bin_ex(target):
    # target을 정수부와 소수부로 구분한다
    i = int(target)     # 정수부
    f = target - i      # 소수부

    # 정수부를 2진수로 변환
    a = []      # 나머지를 넣을 리스트

    # 나눗셈의 몫이 0이 될 때까지
    while i != 0:
        a.append(i % 2)     # 나머지
        i = i // 2          # 몫

    # 요소를 역순으로 바꾼다
    a.reverse()

    #소수부를 2진수로 변환
    b = []      # 정수부를 넣을 리스트
    n = 0       # 반복한 횟수

    # 2를 곱한 후에 얻어진 소수부가 0이 될 때까지
    while (f != 0):
        temp = f * 2            # 소수부×2
        b.append(int(temp))     # 정수부
        f = temp - int(temp)    # 소수부
        n += 1
        if (n >= 10):
            break

    # 2진수로 변환한 값
    return a, b



# 10진수 ‘10.625’를 2진수로 변환한다
print(dec2bin_ex(10.625))
