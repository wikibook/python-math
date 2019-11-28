def dec2bin(target):
    remainder = []      # 나머지를 넣을 리스트

    while target != 0:
        remainder.append(target % 2)        # 나머지
        target = target // 2                # 몫

    # 리스트에 있는 요소를 역순으로 바꿔서 반환한다
    remainder.reverse()
    return remainder



# dec2bin() 함수를 이용해 10진수 26을 2진수로 변환한다
print(dec2bin(26))
# 파이썬에 내장된 bin() 함수를 이용해 26을 2진수로 변환한다
print(bin(26))
