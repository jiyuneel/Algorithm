import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = list()
    for _ in range(N):
        rank.append(tuple(map(int, input().split())))
    rank.sort()

    tmp = rank[0][1]
    cnt = 1
    for r1, r2 in rank:
        if tmp > r2:
            cnt += 1
            tmp = r2
    print(cnt)
