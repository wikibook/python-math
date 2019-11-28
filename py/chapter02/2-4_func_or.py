def func_or():
    a = input('개를 좋아하십니까?（Y/N）... ')   # 키 입력을 부탁하는 메시지를 표시한다
    if (a == 'Y') or (a == 'y'):  	#  ‘Y’ 또는 ‘y’가 입력됐을 때
        print('예')
    else:                       	# 위의 모든 조건을 만족하지 않을 경우
        print('아니오')



func_or()
