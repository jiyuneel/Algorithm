import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maze = list()
for _ in range(N):
    maze.append(list(map(int, input().strip())))
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

print(maze[N - 1][M - 1])
