import sys
input = sys.stdin.readline

n = int(input())
sq = list()
for _ in range(n):
    sq.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
for r in range(n):
    for c in range(r + 1):
        if r == 0:
            dp[r][c] = sq[r][c]
        elif c == 0:
            dp[r][c] = dp[r - 1][c] + sq[r][c]
        elif c == n - 1:
            dp[r][c] = dp[r - 1][c - 1] + sq[r][c]
        else:
            dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c]) + sq[r][c]

print(max(dp[-1]))
