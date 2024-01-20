import sys
input = sys.stdin.readline
from collections import deque

def bfs(building, visited, start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]][start[2]] += 1

    while queue:
        l, r, c = queue.popleft()
        for i in range(6):
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] == '.' and visited[nl][nr][nc] == 0:
                    queue.append((nl, nr, nc))
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                
                elif building[nl][nr][nc] == 'E':
                    return visited[l][r][c]
    return -1

dl = [0, 0, 0, 0, -1, 1]
dr = [0, 0, -1, 1, 0, 0]
dc = [-1, 1, 0, 0, 0, 0]

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    building = list()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    
    for _ in range(L):
        data = list()
        for _ in range(R):
            data.append(list(input().strip()))
        input()
        building.append(data)
    
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    s = (l, r, c)
    
    time = bfs(building, visited, s)
    if time == -1:
        print("Trapped!")
    else:
        print("Escaped in", time, "minute(s).")
