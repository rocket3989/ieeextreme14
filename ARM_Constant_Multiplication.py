# Collin Pearce 39.8% (approx question)

# decompose each number into binary, then add itself to itself each time there is a one, 
# shifting for each location

def MOV(a, b, s):
    print(f'MOV {a}, {b}, LSL #{s}')

def ADD(a, b, c, s):
    print(f'ADD {a}, {b}, {c}, LSL #{s}')


for tc in range(int(input())):
    
    n = int(input())
    
    s = bin(n)[2:]
    
    if n == 0:
        print(f'SUB R0, R0, R0, LSL #0')
        print("END")
        continue
    
    diffs = []
    curr = 0
    for val in s[1:]:
        if val == '1':
            diffs.append(curr + 1)
            curr = 0
        else:
            curr += 1
    if diffs:
        MOV('R1', 'R0', 0)
    
    for val in diffs:
        ADD('R0', 'R1', 'R0', val)
    
    if curr:
        MOV('R0', 'R0', curr)
    
    print("END")