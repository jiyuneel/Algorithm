import sys
input = sys.stdin.readline

A = int(input())
arr = list(map(int, input().split()))
dp = [1] * A

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
