import sys
input=sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1, N + 1):
    graph[i].sort(reverse=True)

visited = [0] * (N + 1)
cnt = 1

def bfs(V):
    global cnt
    queue = deque([V])
    visited[V] = cnt

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

bfs(R)
for i in range(1, N + 1):
    print(visited[i])
