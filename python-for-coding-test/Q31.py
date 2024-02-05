import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    gold = list()
    for i in range(n):
        gold.append(arr[i * m: (i + 1) * m])

    dp = [[0] * m for _ in range(n)]
    for c in range(m):
        for r in range(n):
            if c == 0:
                dp[r][c] = gold[r][c]
            
            elif r == 0:
                dp[r][c] = max(dp[r][c - 1], dp[r + 1][c - 1]) + gold[r][c]
            elif r == n - 1:
                dp[r][c] = max(dp[r - 1][c - 1], dp[r][c - 1]) + gold[r][c]
            else:
                dp[r][c] = max(dp[r - 1][c - 1], dp[r][c - 1], dp[r + 1][c - 1]) + gold[r][c]

    res = 0
    for r in range(n):
        res = max(res, dp[r][-1])
    print(res)
