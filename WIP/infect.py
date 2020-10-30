N, M = [int(x) for x in input().split()]

adj = [[] for i in range(N + 1)]

for i in range(M):
    u, v = [int(x) for x in input().split()]
        
    adj[u].append(v)
    
    adj[v].append(u)

visited = []
    
def dfs(node, S):
    if node == S: return True
    visited[node] = True
    
    found = False
    for other in adj[node]:
        if not visited[other]:
            found = found or dfs(other, S)
    
    return found

for q in range(int(input())):
    F, S = [int(x) for x in input().split()]
    
    
    count = 2
    for i in range(1, N + 1):
        if i == F or i == S: continue
        visited = [False for i in range(N + 1)]
        visited[i] = True
        
        if not dfs(F, S):
            count += 1
    
    print(count)
        
        