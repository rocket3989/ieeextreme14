# Collin Pearce, 100%

# it helps to have already written the relevent code!
# check out IBM ponderthis

# simulate the described sequences

b, d = input().split(';')

N, M = [int(x) for x in input().split()]

birth = [int(x) for x in b]
death = [int(x) for x in d]

mat = []

for i in range(N):
    mat.append([int(x) for x in input()])

for i in range(M):

    neighbors = [[0 for i in range(N)] for j in range(N)]
    
    for r in range(N):
        for c in range(N):
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                R = (r + dr) % N
                C = (c + dc) % N
                
                if mat[R][C]:
                    neighbors[r][c] += 1  
                    
    for r in range(N):
        for c in range(N):
            if mat[r][c]:
                if death[neighbors[r][c]] == 0:
                    mat[r][c] = 0
            
            else:
                if birth[neighbors[r][c]]:
                    mat[r][c] = 1
        
for row in mat:
    print(*row, sep='')
