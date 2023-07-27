N, M = map(int, input().split())
num = list()

def backtracking(n):
    if len(num) == M:
        print(' '.join(map(str, num)))
        return
    for i in range(n, N + 1):
        num.append(i)
        backtracking(i)
        num.pop()

backtracking(1)
