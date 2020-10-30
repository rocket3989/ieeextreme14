# Collin Pearce, 100%
# performance, O(n)


# Need to find all pairs of codes that are one char apart
# approach is to build a mapping of codes with every char replaced with a wildcard
# then count unique pairs

# unique pairs could be counted at end, with (N * (N - 1)) // 2, 
# or simply count how many exist when adding to the map


from collections import defaultdict

coupons = defaultdict(int)

count = 0

for i in range(int(input())):
    code = ''.join(input().split('-'))
    
    for j in range(12):
        curr = list(code)
        curr[j] = '!'
        curr = ''.join(curr)    
        
        count += coupons[curr]
        coupons[curr] += 1
        
print(count)

