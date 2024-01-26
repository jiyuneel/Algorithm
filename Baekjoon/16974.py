import sys
input = sys.stdin.readline

def total_len(level):
    if level == 0:
        return 1
    return total_len(level - 1) * 2 + 3

def patty_len(level):
    if level == 0:
        return 1
    return patty_len(level - 1) * 2 + 1

N, X = map(int, input().split())
X -= 1
total = total_len(N)
patty = patty_len(N)

cnt = 0
while True:
    if X == 0:
        if N == 0:
            cnt += 1
        break
    elif X == total - 1:
        cnt += patty
        break

    if X < total // 2:
        X -= 1
        total = (total - 2) // 2
        patty = patty // 2
    elif X == total // 2:
        cnt += patty // 2 + 1
        break
    else:
        cnt += patty // 2 + 1
        X -= total // 2 + 1
        total = (total - 2) // 2
        patty = patty // 2

    N -= 1

print(cnt)

# P
# B P P P B 3 5
# B BPPPB P BPPPB B 7 13
# B BBPPPBPBPPPBB P BBPPPBPBPPPBB B 15 29
# B BBBPPPBPBPPPBBPBBPPPBPBPPPBBB P BBBPPPBPBPPPBBPBBPPPBPBPPPBBB B 31 61
