import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1, N + 1):
    graph[i].sort(reverse=True)

visited = [0] * (N + 1)
cnt = 0
def dfs(V):
    global cnt
    cnt += 1
    visited[V] = cnt

    for i in graph[V]:
        if not visited[i]:
            dfs(i)

dfs(R)
for i in range(1, N + 1):
    print(visited[i])
