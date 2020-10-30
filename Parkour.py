# Collin Pearce 20% (rest TLE)

# generate queries as described

# BFS from source tile and try to reach destination

# for test case with dist <= 4, could generate 4 DSUs and test against them

N, Q, S, M = [int(x) for x in input().split()]

stableList = []

for i in range(N):
    stableList.append(tuple(int(x) for x in input().split()))
    

params = [int(x) for x in input().split()]  

from collections import deque

def process(s, t, k):
    Q = deque(((s),))
    rem = set(range(1, len(stableList) + 1))
    
    while Q:
        node = Q.popleft()
        
        if node == t: return True
        
        if node not in rem: continue
        rem.remove(node)
        
        for other in rem:
            if abs(stableList[other - 1][0] - stableList[node - 1][0]) + abs(stableList[other - 1][1] - stableList[node - 1][1]) <= k:
                Q.append(other)
            
    return False
        

history = [[0, 0, 0], [0, 0, 0]]
curr = 1
score = 0
MOD = 10 ** 9 + 7

for i in range(S):
    s, t, k = [int(x) for x in input().split()]
    
    history[1] = history[0]
    history[0] = [s, t, k]
    if process(s, t, k + 1):
        score += pow(2, curr, MOD)
        score %= MOD
    curr += 1

while curr <= Q:
    s = (params[0]*history[0][0] + params[1]*history[1][0]+params[2]) % N
    t = (params[3]*history[0][1] + params[4]*history[1][1]+params[5]) % N
    k = (params[6]*history[0][2] + params[7]*history[1][2]+params[8]) % M
    s += 1
    t += 1
    
    
    history[1] = history[0]
    history[0] = [s, t, k]
    if process(s, t, k + 1):
        score += pow(2, curr, MOD)
        score %= MOD
    curr += 1
    
print(score)
    
    