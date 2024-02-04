import sys
input = sys.stdin.readline

N = int(input())
energy = list()
for _ in range(N - 1):
    energy.append(tuple(map(int, input().split())))
K = int(input())

def sol():
    if N == 1:
        return 0

    dp = [0] * N
    dp[1] = energy[0][0]
    superjump = -1
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + energy[i - 1][0], dp[i - 2] + energy[i - 2][1])
        
        if i >= 3:
            tmp = [0] * N
            tmp[i] = dp[i - 3] + K
            if i < N - 1:
                tmp[i + 1] = tmp[i] + energy[i][0]
                for j in range(i + 2, N):
                    tmp[j] = min(tmp[j - 1] + energy[j - 1][0], tmp[j - 2] + energy[j - 2][1])

            if superjump < 0:
                superjump = tmp[N - 1]
            else:
                superjump = min(superjump, tmp[N - 1])

    if N <= 3:
        return dp[N - 1]
    else:
        return min(superjump, dp[N - 1])

print(sol())
