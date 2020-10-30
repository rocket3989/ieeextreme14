# Collin Pearce, 67% (rest WA)

# assume the tiles fit evenly into the given shape
# find the cost of a single tile, then multiply by the
# dim. of the grid in tiles


N, M, R, C = [int(x) for x in input().split()]

tileSum = 0
tiling = []
for i in range(R):
    tiling.append([int(x) for x in input().split()])
    tileSum += sum(tiling[-1])

print(tileSum * (N // R) * (M // C))