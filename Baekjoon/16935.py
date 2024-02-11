import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(list(map(int, input().split())))
operation = list(map(int, input().split()))

def operate1(arr, row):
    for i in range(row // 2):
        arr[i], arr[row - 1 - i] = arr[row - 1 - i], arr[i]
    return arr

def operate2(arr, row, col):
    for i in range(row):
        for j in range(col // 2):
            arr[i][j], arr[i][col - 1 - j] = arr[i][col - 1 - j], arr[i][j]
    return arr

def operate3(arr, row, col):
    new_arr = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            new_arr[j][row - 1 - i] = arr[i][j]
    return new_arr

def operate4(arr, row, col):
    new_arr = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            new_arr[col - 1 - j][i] = arr[i][j]
    return new_arr

def operate5(arr, row, col):
    new_arr = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if i < row // 2:
                # 1번 그룹
                if j < col // 2:
                    new_arr[i][j + col // 2] = arr[i][j]
                # 2번 그룹
                else:
                    new_arr[i + row // 2][j] = arr[i][j]
            else:
                # 3번 그룹
                if j >= col // 2:
                    new_arr[i][j - col // 2] = arr[i][j]
                # 4번 그룹
                else:
                    new_arr[i - row // 2][j] = arr[i][j]
    return new_arr

def operate6(arr, row, col):
    new_arr = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if i < row // 2:
                # 1번 그룹
                if j < col // 2:
                    new_arr[i + row // 2][j] = arr[i][j]
                # 2번 그룹
                else:
                    new_arr[i][j - col // 2] = arr[i][j]
            else:
                # 3번 그룹
                if j >= col // 2:
                    new_arr[i - row // 2][j] = arr[i][j]
                # 4번 그룹
                else:
                    new_arr[i][j + col // 2] = arr[i][j]
    return new_arr

for o in operation:
    if o == 1:
        arr = operate1(arr, N)
    elif o == 2:
        arr = operate2(arr, N, M)
    elif o == 3:
        arr = operate3(arr, N, M)
        N, M = M, N
    elif o == 4:
        arr = operate4(arr, N, M)
        N, M = M, N
    elif o == 5:
        arr = operate5(arr, N, M)
    elif o == 6:
        arr = operate6(arr, N, M)

for row in arr:
    for num in row:
        print(num, end=' ')
    print()
