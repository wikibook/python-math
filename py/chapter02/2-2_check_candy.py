def check_candy(item):
    if (item & 0b1000) != 0:   # 사탕 플래그가 셋팅돼 있는지 확인한다
        print('가지고 있다')
    else:
        print('가지고 있지 않다')



gildong_item = 9
check_candy(gildong_item)
