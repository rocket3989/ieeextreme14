# Collin Pearce 100%
# performance O(log(n))

# all states with less tables than the optimal are correct states
# all states with more tables than the optimal are incorrect states

# therefore, the state space can be binary searched
# mid represents the number of tables produced
# pockets available are total_pockets - tables (the unavailable pockets are holding tables)
# wood that needs to be stored in pockets is total_wood - (tables * table_cost)
# state is valid if all wood can be stored in available pockets
# pocket_space * pockets >= wood

# if the state is valid, the answer is current state or something larger, so left_bound is set to mid
# if the state is not valid, the answer is something smaller, so right_bound is set to mid - 1
# repeat until one value is left (the best one)


C, N, P, W = [int(x) for x in input().split()]

l, r = 0, W // C

while l != r:
    mid = (1 + l + r) // 2
    
    pockets = (N - mid)
    wood = W - (mid * C)
    
    if P * pockets >= wood:
        l = mid
    else:
        r = mid - 1

print(l)