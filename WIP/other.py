n, m = [int(x) for x in input().split()]

graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

time = 0
ans = set()
def bridge(): 
    visited = [False] * (n+1) 
    disc = [float("Inf")] * (n+1) 
    low = [float("Inf")] * (n+1) 
    parent = [-1] * (n+1) 

    for i in range(1, n+1): 
        if not visited[i]: 
            bridgeUtil(i, visited, parent, low, disc)

cuts = set()
def bridgeUtil(u, visited, parent, low, disc):
    global time 
    visited[u]= True
    disc[u] = time 
    low[u] = time 
    time += 1

    for v in graph[u]: 
        if visited[v] == False : 
            parent[v] = u 
            bridgeUtil(v, visited, parent, low, disc) 

            low[u] = min(low[u], low[v]) 
            if low[v] > disc[u]: 
                cuts.add(tuple(sorted((u, v))))
        elif v != parent[u]: 
            low[u] = min(low[u], disc[v]) 
  
bridge()

# print(cuts)
visited = [False for i in range(n+1)]
def dfs(node, parent, dest):
    # print(node, parent)
    visited[node] = True
    global ans
    
     
    
    if node == dest:
        if tuple(sorted((parent, node))) in cuts:
            ans.add(parent)
        return True
        
    found = False
    for other in graph[node]:
        if not visited[other]:
            found = found or dfs(other, node, dest)
    
    # if found: print(tuple(sorted((parent, node))))
    if found and tuple(sorted((parent, node))) in cuts:
        ans.add(parent)
        ans.add(node)
        
    return found
    
# print(cuts)
for tc in range(int(input())):
    visited = [False for i in range(n+1)]

    a, b = [int(x) for x in input().split()]
    # print(a, b)
    ans = set()
    ans.add(a)
    ans.add(b)
    if not dfs(a, -1, b):
        print(n)
    else:
        print(len(ans))