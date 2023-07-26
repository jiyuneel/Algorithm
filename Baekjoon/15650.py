N, M = map(int, input().split())
num = list()

def backtracking(n):
    if len(num) == M:
        print(' '.join(map(str, num)))
        return
    for i in range(n + 1, N + 1):
        if i not in num:
            num.append(i)
            backtracking(i)
            num.pop()

backtracking(0)
