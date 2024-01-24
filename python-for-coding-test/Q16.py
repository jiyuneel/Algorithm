import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
data = list()
for _ in range(N):
    data.append(list(map(int, input().split())))

empty = list()
virus = list()
for y in range(N):
    for x in range(M):
        if data[y][x] == 0:
            empty.append((x, y))
        elif data[y][x] == 2:
            virus.append((x, y))
walls = list(combinations(empty, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
for wall in walls:
    tmp = copy.deepcopy(data)
    for x, y in wall:
        tmp[y][x] = 1

    queue = deque(virus)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = 2
                    queue.append((nx, ny))

    cnt = 0
    for row in tmp:
        cnt += row.count(0)
    res = max(res, cnt)

print(res)
