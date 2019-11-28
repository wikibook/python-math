import matplotlib.pyplot as plt
from PIL import Image

# 이미지를 읽어들인다
src_img = Image.open('sample.png')
plt.imshow(src_img)
plt.show()

# 이미지 크기
width, height = src_img.size

# 출력을 위해 영역을 할당한다
dst_img = Image.new('RGB', (width, height))

# 컬러 -> 흑백
src_img = src_img.convert("L")

# 윤곽 추출
for y in range(0, height-1):
    for x in range(0, width-1):
        # 밝기의 차를 조사한다
        diff_x = src_img.getpixel((x+1, y)) - src_img.getpixel((x, y))
        diff_y = src_img.getpixel((x, y+1)) - src_img.getpixel((x, y))
        diff = diff_x + diff_y

        # 출력
        if diff >= 20:
            dst_img.putpixel((x, y), (255, 255, 255))
        else:
            dst_img.putpixel((x, y), (0, 0, 0))
plt.imshow(dst_img)
plt.show()
