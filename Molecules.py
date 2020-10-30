# Collin Pearce, 50% (rest TLE)

# BFS around the starting state, searching for a valid state
# whichever state is found first is the closest

def valid(C, H, O):
    CO2 = (O - (H // 2)) // 2

    C -= CO2
    O -= 2 * CO2

    glucose = C // 6

    C -= 6 * glucose
    O -= 6 * glucose
    H -= 12 * glucose

    water = H // 2

    H -= 2 * water
    O -= water
    
    return O == 0 and C == 0 and H == 0 and CO2 >= 0 and glucose >= 0 and water >= 0
    

from collections import deque

for tc in range(int(input())):
    C, H, O = [int(x) for x in input().split()]
    Q = deque(((C, H, O),))
    
    seen = set()
    while Q:
        c, h, o = Q.popleft()
        if (c, h, o) in seen or c < 0 or h < 0 or o < 0:
            continue
            
        if valid(c, h, o):
            print(abs(o-O) + abs(H-h) + abs(c-C))
            break
        
        
        Q.append((c + 1, h, o))
        Q.append((c - 1, h, o))
        
        Q.append((c, h + 1, o))
        Q.append((c, h - 1, o))

        Q.append((c, h, o + 1))
        Q.append((c, h, o - 1))
        seen.add((c, h, o))

        