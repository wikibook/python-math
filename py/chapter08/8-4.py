def calc_area(dx):
    h = 0     # 막대의 높이
    area = 0  # 면적
    cnt = int(10 / dx)  # 막대의 개수
    for i in range(1, cnt+1):
        h = i * dx     # 높이를 구한다
        s = h * dx     # 막대의 면적을 구한다
        area += s      # 면적의 합계를 구한다
    return area

print(calc_area(1))
