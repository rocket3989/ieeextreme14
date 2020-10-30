# Collin Pearce 100%

# this is a construction problem
# all numbers > 3 are valid 
# the program starts out with a valid grid of size 4
# then the 'pieces' are extended out, and a new piece is added in the bottom right

base = [[1, 2, 2, 2], [1, 2, 3, 3], [1, 4, 3, 3], [1, 4, 4, 4]]

import string

for i in range(5, 63):
    base.append([1])

    for j in range(4, i, 2):
        base[-1].append(j)
        
    base[-1].extend([i] * ((i) // 2))

    base[0].append(2)
    base[1].append(3)

    pos = 2
    for j in range(5, i, 2):
        base[pos].append(j)
        pos += 1
    
    while pos < i:
        base[pos].append(i)
        pos += 1
    
for tc in range(int(input())):
    N = int(input())
    
    lookup = ' ' + string.ascii_letters + string.digits
    
    if N < 4:
        print('impossible')
        
    else:
        for row in base[:N]:
            print(*[lookup[val] for val in row[:N]], sep='')