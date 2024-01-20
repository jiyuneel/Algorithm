import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque

def bfs(data, visited):
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and data[r][c] == 1:
                queue = deque()
                visited[r][c] = True
                queue.append((r, c))
                global cnt
                cnt += 1

                area = 0
                while queue:
                    area += 1
                    row, col = queue.popleft()

                    for i in range(4):
                        nr = row + dr[i]
                        nc = col + dc[i]

                        if 0 <= nc < m and 0 <= nr < n:
                            if data[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))

                global max_area
                if area > max_area:
                    max_area = area

def dfs(data, visited, row, col):
    global area
    area += 1
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if data[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(data, visited, nr, nc)

data = list()
n, m = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

cnt, max_area = 0, 0

# bfs
bfs(data, visited)
# dfs
for r in range(n):
    for c in range(m):
        if data[r][c] == 1 and not visited[r][c]:
            cnt += 1
            area = 0
            visited[r][c] = True
            dfs(data, visited, r, c)
            if area > max_area:
                max_area = area

# print(cnt)
# print(max_area)
