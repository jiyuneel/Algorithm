import sys
input = sys.stdin.readline

C, N = map(int, input().split())
city = list()
for _ in range(N):
    city.append(tuple(map(int, input().split())))
city.sort(key=lambda x: x[1])

dp = [100 * C] * (C + city[-1][1])
for m, p in city:
    dp[p] = min(dp[p], m)

for i in range(1, C + city[-1][1]):
    for m, p in city:
        if i - p > 0 and dp[i - p] != 0:
            dp[i] = min(dp[i], dp[i - p] + m)
print(min(dp[C:]))
