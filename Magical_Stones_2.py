# Marcos Duran, 25%

# when in doubt, guess

# simulates random choices in the game
# if the choices lead to the single stone state after a set number of moves, 
# print the choices made, else print impossible



from random import randint
for tc in range(int(input())):
    N  = int(input())
    
    W = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    
    arr = [int(i) for i in range(1, N+1)]
    
    count = 0
    ans = ""
    while count <= 10000:
        
        magic = randint(0, 1)
        
        if not magic: #white
            curr = set()
            
            for val in arr:
                curr.add(W[val-1])
            # print("white:", curr)
            ans += "W"
            arr = curr
        else:
            curr = set()
            for val in arr:
                curr.add(B[val-1])
            ans += "B"
            arr = curr
            # print("black:", curr)
        
        if len(curr) < 2: break
        
        count += 1
    
    if count > 10000:
        print("impossible")
    else:
        print(ans)