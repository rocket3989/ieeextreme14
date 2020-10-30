


for tc in range(int(input())):
    C, H, O = [int(x) for x in input().split()]
    
    used = 0    
    
    if H & 1:
        used += 1
        H += 1
    
    water = H // 2
    
    O -= water
    
    if O < 0:
        used -= O
        O = 0
        
    if O
    
    C -= O // 2