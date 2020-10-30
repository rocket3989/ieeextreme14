# Collin Pearce, 100%

# travel through array, building out odd and then even length palindromes
# on the left side of the palindrome, mark the max length of a palindrome that started there
# on the right side of the palindrome, mark the max length of a palindrome that ended there

# then traverse those arrays, and keep the largest start + end that came before it



for tc in range(int(input())):
    S = input()
    N = len(S)
    
    max_length = [1 for i in range(N)]
    max_length[0] = -N
    
    best_start = [1 for i in range(N)]
    best_start[-1] = -N
    
    for i in range(N):
        offset = 0
        while i - offset >= 0 and i + offset < N and S[i - offset] == S[i + offset]:
            max_length[i + offset] = max(max_length[i + offset], 1 + 2 * offset)
            best_start[i - offset] = max(best_start[i - offset], 1 + 2 * offset)
            
            offset += 1

    for i in range(N):
        offset = 0
        while i - offset >= 0 and i + offset - 1 < N and S[i - offset] == S[i + offset - 1]:
            max_length[i + offset - 1] = max(max_length[i + offset - 1], 2 * offset)
            best_start[i - offset] = max(best_start[i - offset], 2 * offset)
            offset += 1
            
    
    best = 0
    bestPre = -N
    for a, b in zip([-N] + max_length, best_start):
        bestPre = max(bestPre, a)
        best = max(best, bestPre + b)
    
    print(best)
    