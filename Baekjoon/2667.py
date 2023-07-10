import sys
input=sys.stdin.readline

N = int(input())
map = list()
for i in range(N):
    map.append(list(int(x) for x in list(input().strip())))

complex = list()
cnt = 0
def dfs(x, y):
    global cnt
    map[x][y] = 0
    cnt += 1

    if x + 1 < N and map[x + 1][y]:
        dfs(x + 1, y)
    if x - 1 >= 0 and map[x - 1][y]:
        dfs(x - 1, y)
    if y + 1 < N and map[x][y + 1]:
        dfs(x, y + 1)
    if y - 1 >= 0 and map[x][y - 1]:
        dfs(x, y - 1)

for x in range(N):
    for y in range(N):
        if map[x][y]:
            cnt = 0
            dfs(x, y)
            complex.append(cnt)
complex.sort()

print(len(complex))
for x in complex: print(x)
