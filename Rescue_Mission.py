# Collin Pearce, 100%
# performance, O(d + n log*n)

# since all information is avaliable before a plan has to be made,
# there is no reason to make a plan at all. 
# keep track of sets of nodes that a soldier *could* have travelled between
# everytime two nodes are fogged over together, merge them into one new node
# this is called disjoint set union, or DSU

# track how many soldiers are in each disjoint set, and evacuate the max possible
# when a vehicle is there

# just using DSU isn't fast enough, as each cell in each day's range has to be merged
# and each day's range could be the entire range of days, leading to O(d * n log*n) worst case
# luckily, each day's range is continuous, so the disjoint set can include a right_bound
# to indicate where it ends. Now only cells outside of the current range will be merged.


N = int(input())

soldiers = [0] + [int(x) for x in input().split()]

saved = 0

parent = list(range(N + 1))
right_bound = list(range(N + 1))

def parOf(node):
    if node != parent[node]:
        parent[node] = parOf(parent[node])
	
    return parent[node]


for day in range(int(input())):
    l, r, V = [int(x) for x in input().split()]
    
    x = parOf(l)

    bound = right_bound[x] + 1

    while bound <= r:
        y = parOf(bound)

        soldiers[x] += soldiers[y]
        parent[y] = x
        right_bound[x] = right_bound[y]
            
        bound = right_bound[x] + 1
        
    curr = min(soldiers[x], V)
    soldiers[x] -= curr
    
    saved += curr
    
print(saved)