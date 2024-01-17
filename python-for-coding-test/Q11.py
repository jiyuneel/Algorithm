import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())

apple = set()
for _ in range(K):
    r, c = map(int, input().split())
    apple.add((r, c))

L = int(input())
rotate = dict()
for _ in range(L):
    X, C = input().split()
    rotate[int(X)] = C
rotate_sec = rotate.keys()

snake = deque()
snake.append((1, 1))
dr = deque([0, 1, 0, -1])
dc = deque([1, 0, -1, 0])

sec = 0
while True:
    sec += 1
    head = (snake[0][0] + dr[0], snake[0][1] + dc[0])
    if not (1 <= head[0] <= N) or not (1 <= head[1] <= N) or head in snake:
        break
    
    # 이동한 칸에 사과가 있다면
    if head in apple:
        apple.remove(head)
    # 이동한 칸에 사과가 없다면
    else:
        snake.pop()
    snake.appendleft(head)

    if sec in rotate_sec:
        # 왼쪽으로 회전
        if rotate[sec] == 'L':
            dr.rotate(1)
            dc.rotate(1)
        # 오른쪽으로 회전
        elif rotate[sec] == 'D':
            dr.rotate(-1)
            dc.rotate(-1)

print(sec)
