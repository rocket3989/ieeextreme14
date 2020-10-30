# Collin Pearce 100%
# performance O(n log(n))

# when a switch is flipped, all of the lights are inverted
# exactly K switches have to be flipped
# greedily choose the floors with the least lights on to be flipped first
# this will maximise the total lights on


for tc in range(int(input())):
    M, N, K = [int(x) for x in input().split()]
    
    floors = []
    
    for i in range(M):
        floors.append(int(input()))
        
    floors.sort()
    
    for i in range(K):
        floors[i] = N - floors[i]
        
    print(sum(floors))