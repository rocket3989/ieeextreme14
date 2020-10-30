# Collin Pearce, Marcos Duran 72%

# simulate the given process, saving the least time taken to 
# reach each length. Query the saved values


n = int(input())

arr = [int(x) for x in input().split()]
num = [i for i in range(1, n + 1)]

dp = [-1 for i in range(n + 1)]
dp[n] = 0

length = n

for step in range(1, n + 1):

    curr = set()
    for val in num:
        curr.add(arr[val - 1])

    length = len(curr)
    dp[length] = step if dp[length] == -1 else dp[length]
    
    num = curr

for tc in range(int(input())):
    k = int(input())
    print(dp[k])