import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0

queue = deque([X])
while queue:
    city = queue.popleft()
    for i in graph[city]:
        if distance[i] == -1:
            distance[i] = distance[city] + 1
            queue.append(i)

res = False
for city in range(1, N + 1):
    if distance[city] == K:
        print(city)
        res = True

if res == False:
    print(-1)
