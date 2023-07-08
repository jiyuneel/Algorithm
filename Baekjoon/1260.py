import sys
input=sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1, N + 1):
    graph[i].sort()

visitedDFS = [False] * (N + 1)
visitedBFS = [False] * (N + 1)

def dfs(graph, visited, V):
    visited[V] = True
    print(V, end=' ')

    for i in graph[V]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, V):
    queue = deque([V])
    visited[V] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, visitedDFS, V)
print()
bfs(graph, visitedBFS, V)
print()
