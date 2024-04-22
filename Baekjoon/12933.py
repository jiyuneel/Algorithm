import sys
input = sys.stdin.readline

sound = input().strip()
quack = [0] * 5

is_quack = True
for c in sound:
    if c == 'q':
        quack[0] += 1
        if quack[4]:
            quack[4] -= 1
    elif c == 'u':
        if quack[0]:
            quack[0] -= 1
            quack[1] += 1
        else:
            is_quack = False
    elif c == 'a':
        if quack[1]:
            quack[1] -= 1
            quack[2] += 1
        else:
            is_quack = False
    elif c == 'c':
        if quack[2]:
            quack[2] -= 1
            quack[3] += 1
        else:
            is_quack = False
    elif c == 'k':
        if quack[3]:
            quack[3] -= 1
            quack[4] += 1
        else:
            is_quack = False
    else:
        is_quack = False

    if not is_quack:
        break

if quack[0] or quack[1] or quack[2] or quack[3]:
    is_quack = False

if is_quack:
    print(quack[4])
else:
    print(-1)
