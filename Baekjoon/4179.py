import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
maze = list()
for _ in range(R):
    maze.append(list(input().strip()))

player = tuple()
fire = deque()
fire_time = list([-1] * C for _ in range(R))
visited = [[False] * C for _ in range(R)]

for row in range(R):
    for col in range(C):
        if maze[row][col] == 'J':
            player = (row, col, 0)
            visited[row][col] = True
        elif maze[row][col] == 'F':
            fire.append((row, col))
            fire_time[row][col] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 불 확산 시간 계산
while fire:
    row, col = fire.popleft()
    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if maze[nr][nc] != '#' and fire_time[nr][nc] == -1:
                fire_time[nr][nc] = fire_time[row][col] + 1
                fire.append((nr, nc))

def bfs():
    player_q = deque()
    player_q.append(player)
    while player_q:
        row, col, time = player_q.popleft()
        time += 1
        if row == 0 or row == R - 1 or col == 0 or col == C - 1:
            return time

        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if (fire_time[nr][nc] == -1 or fire_time[nr][nc] > time) and maze[nr][nc] == '.':
                    visited[nr][nc] = True
                    player_q.append((nr, nc, time))

    return "IMPOSSIBLE"

print(bfs())
