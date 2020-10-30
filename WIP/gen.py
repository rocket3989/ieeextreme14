n = 100

from random import randrange

edges = set()

def orderPair(a, b):
    return tuple(sorted((a, b)))


for i in range(1, n + 1):
    for j in range(1):
        other = randrange(1, n + 1)
        if other == i: continue
        edges.add(orderPair(i, other))
        
        
print(n, len(edges))
for edge in edges:
    print(*edge)
    
print((n * (n - 1)) // 2)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        print(i, j)