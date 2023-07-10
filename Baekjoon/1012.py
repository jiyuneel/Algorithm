import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    arr[x][y] = 0
    if x + 1 < N and arr[x + 1][y]:
        dfs(x + 1, y)
    if x - 1 >= 0 and arr[x - 1][y]:
        dfs(x - 1, y)
    if y + 1 < M and arr[x][y + 1]:
        dfs(x, y + 1)
    if y - 1 >= 0 and arr[x][y - 1]:
        dfs(x, y - 1)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y]:
                dfs(x, y)
                cnt += 1
    print(cnt)
