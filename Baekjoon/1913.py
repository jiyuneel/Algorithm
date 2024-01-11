import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
find = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
direction = 0

def fill_graph(x, y, dir, num):
    if num == 0:
        return

    if dir % 4 == 0:
        while y < N and graph[y][x] == 0:
            graph[y][x] = num
            num -= 1
            
            if y == N - 1 or graph[y + 1][x] != 0:
                fill_graph(x + 1, y, dir + 1, num)
            else:
                y += 1
    
    elif dir % 4 == 1:
        while x < N and graph[y][x] == 0:
            graph[y][x] = num
            num -= 1
            
            if x == N - 1 or graph[y][x + 1] != 0:
                fill_graph(x, y - 1, dir + 1, num)
            else:
                x += 1
    
    elif dir % 4 == 2:
        while y >= 0 and graph[y][x] == 0:
            graph[y][x] = num
            num -= 1
            
            if y == 0 or graph[y - 1][x] != 0:
                fill_graph(x - 1, y, dir + 1, num)
            else:
                y -= 1
    
    elif dir % 4 == 3:
        while x >= 0 and graph[y][x] == 0:
            graph[y][x] = num
            num -= 1
            
            if x == 0 or graph[y][x - 1] != 0:
                fill_graph(x, y + 1, dir + 1, num)
            else:
                x -= 1

fill_graph(0, 0, direction, N * N)

for r in graph:
    for c in r:
        print(c, end = " ")
    print()

for r in range(N):
    for c in range(N):
        if graph[r][c] == find:
            print(r + 1, c + 1)
