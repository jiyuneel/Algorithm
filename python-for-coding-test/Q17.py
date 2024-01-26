import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
data = list()
for _ in range(N):
    data.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

queue = deque()
for x in range(N):
    for y in range(N):
        if data[x][y] != 0:
            queue.append((data[x][y], x, y))
# 낮은 번호의 바이러스 순으로 정렬
queue = deque(sorted(queue))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

time = 0
while queue and time != S:
    virus, x, y = queue.popleft()

    if len(queue) == 0 or (queue[0][0] < virus):
        time += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == 0:
                queue.append((data[x][y], nx, ny))
                data[nx][ny] = data[x][y]

print(data[X - 1][Y - 1])
