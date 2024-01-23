import sys
input = sys.stdin.readline
from collections import deque

def bfs(data, queue):
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if data[nz][ny][nx] == 0:
                    data[nz][ny][nx] = data[z][y][x] + 1
                    queue.append((nx, ny, nz))

    day = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if data[z][y][x] == 0:
                    return -1
                day = max(day, data[z][y][x])
    return day - 1


M, N, H = map(int, input().split())
data = list()
for _ in range(H):
    d = list()
    for _ in range(N):
        d.append(list(map(int, input().split())))
    data.append(d)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if data[z][y][x] == 1:
                queue.append((x, y, z))

print(bfs(data, queue))
