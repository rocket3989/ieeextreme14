# Collin Pearce 87% (rest WA)

# written during the contest
# still not sure what causes the errors

# same process as other code, but uses linear time pattern find alg

N, T = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

diffs = []
for a, b in zip(arr, arr[1:]):
    diffs.append(b - a)
    
diffs.append((T - arr[-1]) + (arr[0]))

from collections import deque

nextLook = deque()

for i, el in enumerate(diffs):
    if el == diffs[0]:
        nextLook.append(i)

patternLen = 0

while len(nextLook) > 1 and patternLen * len(nextLook) < N:
    thisLook, nextLook = nextLook, deque()
    

    patternLen += 1
    curr = diffs[(thisLook[0] + patternLen) % N]
    
    lastSeen = thisLook[-1] - N
    
    while len(thisLook):
        pos = thisLook.popleft()
        if pos - lastSeen < patternLen:
            lastSeen = pos
            continue
            
        lastSeen = pos
        
        if diffs[(pos + patternLen) % N] == curr:
            
            nextLook.append(pos)

if len(nextLook) == 0:
    print('here?')
    
if len(nextLook) == 1: patternLen = N

print(patternLen, N, T)

repetitions = N // patternLen

print((T // repetitions) - 1)