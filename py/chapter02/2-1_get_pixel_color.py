def get_pixel_color(c):
    r = (c & 0x00FF0000) >> 16 		# R(빨강)
    g = (c & 0x0000FF00) >> 8  		# G(초록)
    b = (c & 0x000000FF)       		# B(파랑)
    return r, g, b



c = 4287090426
r, g, b = get_pixel_color(c)
print(r, g, b)
