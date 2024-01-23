import sys
input = sys.stdin.readline
from collections import deque

def bfs(box):
    queue = deque()
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                queue.append((r, c))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if box[nr][nc] == 0:
                    box[nr][nc] = box[row][col] + 1
                    queue.append((nr, nc))

    day = 0
    for i in box:
        if 0 in i:
            return -1
        day = max(day, max(i))
    return day - 1


M, N = map(int, input().split())
box = list()
for _ in range(N):
    box.append(list(map(int, input().split())))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

print(bfs(box))
