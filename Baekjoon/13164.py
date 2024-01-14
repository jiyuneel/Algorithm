import sys
input = sys.stdin.readline

N, K = map(int, input().split())
height = list(map(int, input().split()))
diff = list()
for i in range(1, N):
    diff.append(height[i] - height[i - 1])
diff.sort()

cost = 0
for i in range(N - K):
    cost += diff[i]
print(cost)
