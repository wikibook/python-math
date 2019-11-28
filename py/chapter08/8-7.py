from scipy import integrate
import math

# 반지름이 r인 원의 원주를 구한다
def calc_area(r):
    return 2 * math.pi * r

# 반지름이 2～5인 구간에서 원주의 합계
s = integrate.quad(calc_area, 2, 5)
print(s)

# 두루마리 화장지의 길이
x = s[0] / 0.011
print(x)
