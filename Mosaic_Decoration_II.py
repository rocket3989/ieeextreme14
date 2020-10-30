# Marcos Duran, 100%

# tile the field as much as possible, then cut off the extra
# cut along the width if the height isn't evenly divisible, and vice versa

from math import ceil
w, h, a, b, m, c = [int(x) for x in input().split()]

total_tiles = (ceil(w / a) * ceil(h / b))
cost = m * ceil(total_tiles / 10)

if h % b != 0:
    cost += (c * w)
if w % a != 0:
    cost += (c * h)
    
print(cost)