import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
rgb =  list()
for _ in range(N):
    rgb.append(list(input().strip()))
visited = [[False] * N for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy]:
            if rgb[x][y] == rgb[xx][yy]:
                dfs(xx, yy)

res1, res2 = 0, 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            dfs(x, y)
            res1 += 1

for i in range(N):
    for j in range(N):
        if rgb[i][j] == 'G':
            rgb[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            dfs(x, y)
            res2 += 1

print(res1, res2)
