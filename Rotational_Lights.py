# Collin Pearce 100%
# written post-contest

# pull in the light array, and calculate the distance between adjacent lights

# goal is now to find how often that pattern repeats, then the answer is len // repetitions - 1

# rotate copied version of diff array that is in a deque and compare to the original, until a match is found

# that is the distance between repetitions, use that to find count of repetitions

# honesty not sure how this is fast enough, it really doesn't seem like it should be
# but early exits on comparison loops reduce complexity greatly
# this code breaks on an input structured with diffs like AAAAAAAAA....AAAAAC
# the full comparison loop will run N - iteration_count times, so O(n^2)

# print(10000, 10001)
# print(*range(10000))
# will make a tc that breaks this code, but the other version burns right through


N, T = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

diffs = []
for a, b in zip(arr, arr[1:]):
    diffs.append(b - a)
    
diffs.append((T - arr[-1]) + (arr[0]))

from collections import deque

rotated = deque(diffs)

for i in range(1, N + 1):
    rotated.rotate()
    
    for a, b in zip(rotated, diffs):
        if a != b: break
        
    else:
        repetitions = N // i
        print((T // repetitions) - 1)
        break
        