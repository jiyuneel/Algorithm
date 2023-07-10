import sys
input=sys.stdin.readline

N = int(input())
M = int(input())

network = [[] for _ in range(N + 1)]
for _ in range(M):
    c1, c2 = map(int, input().split())
    network[c1].append(c2)
    network[c2]. append(c1)

virus = [False] * (N + 1)
cnt = 0
def dfs(c):
    global cnt
    virus[c] = True

    for i in network[c]:
        if not virus[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)
