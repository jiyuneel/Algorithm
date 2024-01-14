import copy
import sys
input = sys.stdin.readline

# 시계방향 회전
def clockwise(n, arr):
    res = copy.deepcopy(arr)
    for row in range(n):
        for col in range(n):
            if row == col:
                res[row][n // 2] = arr[row][col]
            elif col == n // 2:
                res[row][n - row - 1] = arr[row][col]
            elif row + col == n - 1:
                res[n // 2][col] = arr[row][col]
            elif row == n // 2:
                res[col][col] = arr[row][col]
    return res

# 반시계방향 회전
def counterclockwise(n, arr):
    res = copy.deepcopy(arr)
    for row in range(n):
        for col in range(n):
            if row == col:
                res[n // 2][col] = arr[row][col]
            elif col == n // 2:
                res[row][row] = arr[row][col]
            elif row + col == n - 1:
                res[row][n // 2] = arr[row][col]
            elif row == n // 2:
                res[n - col - 1][col] = arr[row][col]
    return res

T = int(input())
for _ in range(T):
    n, d = map(int, input().split())

    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    if (d >= 0):
        d = d // 45
    else:
        d = (d // 45 + 8) % 8

    if (d <= 4):
        for _ in range(d):
            arr = clockwise(n, arr)
    else:
        for _ in range(8 - d):
            arr = counterclockwise(n, arr)

    for num in arr:
        for n in num:
            print(n, end=' ')
        print()
