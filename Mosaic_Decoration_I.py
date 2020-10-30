# Marcos Duran 100%

# first count how many tiles are used in total
# since piles can only be purchased in increments of 10, 
# the number of piles needed is the ceiling of tiles / 10
# total cost is cost_of_pile * pile_count for each tile


from math import ceil
n, b, p = [int(x) for x in input().split()]

total_black, total_pink = 0, 0

for i in range(n):
    u, v = [int(x) for x in input().split()]
    total_black += u
    total_pink += v

black_piles, pink_piles = ceil(total_black / 10), ceil(total_pink / 10)

print(black_piles * b + pink_piles * p)