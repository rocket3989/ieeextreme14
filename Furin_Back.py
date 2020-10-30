# Iskandar Sobirov, 50% (rest TLE)
 
# give the given code to a brainf*ck interpreter
# hope for the best

from collections import defaultdict

def main():
    line = input()
    index = 0
    data = defaultdict(int)
    index += 1
    for _ in range(1):
        data[index] = ord(line[0])
    index += 1
    for _ in range(1):
        data[index] = ord(line[1])
    index += 1
    for _ in range(1):
        data[index] = ord(line[2])
    index -= 1
    while data[index]:
        data[index] = (data[index] - 1) % 256
        index += 1
        data[index] = (data[index] - 1) % 256
        index += 1
        data[index] = (data[index] + 1) % 256
        index -= 2
    index += 2
    while data[index]:
        data[index] = (data[index] - 1) % 256
        index -= 2
        data[index] = (data[index] + 1) % 256
        index += 2
    index -= 3
    while data[index]:
        data[index] = (data[index] - 1) % 256
        index += 1
        data[index] = (data[index] - 1) % 256
        index -= 2
        data[index] = (data[index] + 1) % 256
        index += 1
    index -= 1
    while data[index]:
        data[index] = (data[index] - 1) % 256
        index += 1
        data[index] = (data[index] + 1) % 256
        index -= 1
    index += 6
    data[index] = (data[index] + 1) % 256
    index += 7
    data[index] = (data[index] + 1) % 256
    while data[index]:
        index += 4
        while data[index]:
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
        index -= 12
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index += 7
            data[index] = (data[index] + 1) % 256
            index += 6
            data[index] = (data[index] + 1) % 256
            index -= 13
        index += 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index += 7
            data[index] = (data[index] + 1) % 256
            index += 6
            data[index] = (data[index] + 1) % 256
            index -= 13
        index += 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index += 7
            data[index] = (data[index] + 1) % 256
            index += 6
            data[index] = (data[index] + 1) % 256
            index -= 13
        index += 2
        data[index] = (data[index] + 1) % 256
        index += 1
        data[index] = (data[index] + 1) % 256
        while data[index]:
            index -= 1
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index += 2
            data[index] = (data[index] + 1) % 256
            index -= 3
        index += 4
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index -= 7
            data[index] = (data[index] + 1) % 256
            index += 7
        index += 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index -= 7
            data[index] = (data[index] + 1) % 256
            index += 7
        index += 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index -= 7
            data[index] = (data[index] + 1) % 256
            index += 7
        index += 7
        data[index] = (data[index] + 1) % 256
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index -= 11
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index += 2
                data[index] = (data[index] + 1) % 256
                index += 2
                data[index] = (data[index] + 1) % 256
                index -= 4
            index += 1
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index += 2
                data[index] = (data[index] + 1) % 256
                index += 2
                data[index] = (data[index] + 1) % 256
                index -= 4
            index += 1
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index -= 2
                data[index] = (data[index] + 1) % 256
                index += 2
            index += 1
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index -= 2
                data[index] = (data[index] + 1) % 256
                index += 2
            data[index] = (data[index] + 1) % 256
            while data[index]:
                while data[index]:
                    data[index] = (data[index] - 1) % 256
                data[index] = (data[index] + 1) % 256
                index += 1
                while data[index]:
                    index -= 1
                    data[index] = (data[index] - 1) % 256
                index -= 1
                while data[index]:
                    data[index] = (data[index] - 1) % 256
                    index += 2
                    data[index] = (data[index] - 1) % 256
                    index -= 3
                index += 2
                data[index] = (data[index] - 1) % 256
                index += 3
                data[index] = (data[index] + 1) % 256
                index += 1
                while data[index]:
                    index -= 1
                    data[index] = (data[index] - 1) % 256
                index -= 1
                while data[index]:
                    data[index] = (data[index] - 1) % 256
                    index += 1
                    data[index] = (data[index] + 1) % 256
                    index += 1
                    while data[index]:
                        data[index] = (data[index] - 1) % 256
                        index -= 1
                        data[index] = (data[index] - 1) % 256
                    index -= 1
                    while data[index]:
                        index += 2
                        while data[index]:
                            data[index] = (data[index] - 1) % 256
                            index -= 2
                            data[index] = (data[index] - 1) % 256
                            index += 1
                        data[index] = (data[index] - 1) % 256
                        index -= 2
                        while data[index]:
                            data[index] = (data[index] - 1) % 256
                            index += 1
                            data[index] = (data[index] - 1) % 256
                            index += 2
                            data[index] = (data[index] - 1) % 256
                            index -= 4
                    index -= 1
                index += 2
                data[index] = (data[index] - 1) % 256
                index -= 5
                data[index] = (data[index] + 1) % 256
                index += 1
                while data[index]:
                    index -= 1
                    data[index] = (data[index] - 1) % 256
                index -= 1
                while data[index]:
                    index += 2
                    while data[index]:
                        index -= 2
                        data[index] = (data[index] - 1) % 256
                        index += 1
                    index -= 2
                    while data[index]:
                        index -= 1
                index += 1
                data[index] = (data[index] - 1) % 256
            index += 8
            data[index] = (data[index] + 1) % 256
        data[index] = (data[index] - 1) % 256
        index -= 4
        data[index] = (data[index] + 1) % 256
        index += 1
        data[index] = (data[index] + 1) % 256
        while data[index]:
            index -= 1
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            index += 2
            data[index] = (data[index] + 1) % 256
            while data[index]:
                index -= 2
                data[index] = (data[index] - 1) % 256
                index += 1
            index -= 2
            while data[index]:
                index += 2
                index += 1
                data[index] = (data[index] + 1) % 256
                while data[index]:
                    index -= 3
                    data[index] = (data[index] - 1) % 256
                    index += 2
                index -= 3
                while data[index]:
                    index -= 1
        index += 1
        data[index] = (data[index] - 1) % 256
    index += 4
    while data[index]:
        data[index] = (data[index] - 1) % 256
    index -= 14
    while data[index]:
        data[index] = (data[index] - 1) % 256
    index += 2
    data[index] = (data[index] + 1) % 256
    index += 1
    data[index] = (data[index] + 1) % 256
    while data[index]:
        index -= 1
        data[index] = (data[index] - 1) % 256
    index -= 1
    while data[index]:
        data[index] = (data[index] - 1) % 256
        index += 2
        data[index] = (data[index] + 1) % 256
        index -= 3
    index += 1
    data[index] = (data[index] + 1) % 256
    index += 1
    while data[index]:
        index -= 1
        data[index] = (data[index] - 1) % 256
    index -= 1
    while data[index]:
        index += 2
        while data[index]:
            index -= 2
            data[index] = (data[index] - 1) % 256
            index += 1
        index -= 2
        while data[index]:
            index -= 1
    index += 1
    data[index] = (data[index] - 1) % 256
    while data[index]:
        data[index] = (data[index] + 1) % 256
        index += 6
        data[index] = (data[index] + 10) % 256
        index -= 6
        data[index] = (data[index] + 1) % 256
        index += 1
        while data[index]:
            index -= 1
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            index += 2
            while data[index]:
                index -= 2
                data[index] = (data[index] - 1) % 256
                index += 1
            index -= 2
            while data[index]:
                index -= 1
        index += 1
        data[index] = (data[index] - 1) % 256
        while data[index]:
            data[index] = (data[index] + 2) % 256
            index += 1
            while data[index]:
                index -= 1
                data[index] = (data[index] - 1) % 256
            index -= 1
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index += 2
                data[index] = (data[index] - 1) % 256
                index -= 3
            index += 2
            data[index] = (data[index] - 1) % 256
            index += 2
            data[index] = (data[index] + 1) % 256
            index += 2
            data[index] = (data[index] + 1) % 256
            index += 1
            data[index] = (data[index] - 1) % 256
            while data[index]:
                index -= 1
                data[index] = (data[index] - 1) % 256
            index -= 1
            while data[index]:
                index -= 2
                while data[index]:
                    data[index] = (data[index] - 1) % 256
                    index += 3
                    data[index] = (data[index] + 1) % 256
                    index -= 3
                index += 5
                data[index] = (data[index] + 1) % 256
                index += 1
                data[index] = (data[index] + 1) % 256
                while data[index]:
                    index -= 1
                    data[index] = (data[index] - 1) % 256
                index -= 1
                while data[index]:
                    data[index] = (data[index] - 1) % 256
                    index += 2
                    data[index] = (data[index] + 1) % 256
                    index -= 3
                index -= 2
                data[index] = (data[index] - 1) % 256
                index -= 1
            index -= 4
            data[index] = (data[index] + 1) % 256
            index += 1
            while data[index]:
                index -= 1
                data[index] = (data[index] - 1) % 256
            index -= 1
            while data[index]:
                index += 2
                while data[index]:
                    index -= 2
                    data[index] = (data[index] - 1) % 256
                    index += 1
                index -= 2
                while data[index]:
                    index -= 1
            index += 1
            data[index] = (data[index] - 1) % 256
        index += 2
        data[index] = (data[index] + 8) % 256
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index += 1
            data[index] = (data[index] + 6) % 256
            index -= 1
        index += 1
        while data[index]:
            data[index] = (data[index] - 1) % 256
            index -= 4
            data[index] = (data[index] + 1) % 256
            index += 4
        index += 5
        data[index] = (data[index] + 1) % 256
        index += 1
        while data[index]:
            index -= 1
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            index += 2
            while data[index]:
                index -= 2
                data[index] = (data[index] - 1) % 256
                index += 1
            index -= 2
            while data[index]:
                index -= 1
        index += 1
        data[index] = (data[index] - 1) % 256
        while data[index]:
            data[index] = (data[index] + 2) % 256
            index += 1
            while data[index]:
                index -= 1
                data[index] = (data[index] - 1) % 256
            index -= 1
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index += 2
                data[index] = (data[index] - 1) % 256
                index -= 3
            index += 2
            data[index] = (data[index] - 1) % 256
            index -= 8
            data[index] = (data[index] + 1) % 256
            index += 1
            data[index] = (data[index] + 1) % 256
            while data[index]:
                index -= 1
                data[index] = (data[index] - 1) % 256
            index -= 1
            while data[index]:
                data[index] = (data[index] - 1) % 256
                index += 2
                data[index] = (data[index] + 1) % 256
                index -= 3
            index += 8
            data[index] = (data[index] + 1) % 256
            index += 1
            while data[index]:
                index -= 1
                data[index] = (data[index] - 1) % 256
            index -= 1
            while data[index]:
                index += 2
                while data[index]:
                    index -= 2
                    data[index] = (data[index] - 1) % 256
                    index += 1
                index -= 2
                while data[index]:
                    index -= 1
            index += 1
            data[index] = (data[index] - 1) % 256
        index -= 2
        while data[index]:
            data[index] = (data[index] - 1) % 256
        index -= 5
        data[index] = (data[index] + 1) % 256
        index += 1
        while data[index]:
            index -= 1
            data[index] = (data[index] - 1) % 256
        index -= 1
        while data[index]:
            index += 2
            while data[index]:
                index -= 2
                data[index] = (data[index] - 1) % 256
                index += 1
            index -= 2
            while data[index]:
                index -= 1
        index += 1
        data[index] = (data[index] - 1) % 256
    index -= 2
    #print(data)
    while data[index]:
        for _ in range(1):
            print(chr(data[index]), end="")
        index -= 1

for tc in range(int(input())):
    main()
    print()