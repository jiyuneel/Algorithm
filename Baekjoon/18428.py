import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
data = list()
for _ in range(N):
    data.append(list(input().split()))

teacher = list()
empty = list()
for row in range(N):
    for col in range(N):
        if data[row][col] == 'T':
            teacher.append((row, col))
        elif data[row][col] == 'X':
            empty.append((row, col))

def sol():
    obstacles = list(combinations(empty, 3))
    for o1, o2, o3 in obstacles:
        tmp = [arr[:] for arr in data]
        tmp[o1[0]][o1[1]] = 'O'
        tmp[o2[0]][o2[1]] = 'O'
        tmp[o3[0]][o3[1]] = 'O'

        cnt = 0
        for t_row, t_col in teacher:
            # 상
            for row in range(t_row - 1, -1, -1):
                if tmp[row][t_col] == 'S':
                    cnt += 1
                    break
                elif tmp[row][t_col] == 'O':
                    break
            # 하
            for row in range(t_row + 1, N):
                if tmp[row][t_col] == 'S':
                    cnt += 1
                    break
                elif tmp[row][t_col] == 'O':
                    break
            # 좌
            for col in range(t_col - 1, -1, -1):
                if tmp[t_row][col] == 'S':
                    cnt += 1
                    break
                elif tmp[t_row][col] == 'O':
                    break
            # 우
            for col in range(t_col + 1, N):
                if tmp[t_row][col] == 'S':
                    cnt += 1
                    break
                elif tmp[t_row][col] == 'O':
                    break
        if cnt == 0:
            return "YES"
    return "NO"

print(sol())
