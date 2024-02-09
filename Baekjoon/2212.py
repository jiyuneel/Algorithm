import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

if N <= K:
    print(0)
else:
    diff = list()
    for i in range(N - 1):
        diff.append(sensor[i + 1] - sensor[i])
    diff.sort(reverse=True)

    for _ in range(K - 1):
        diff.pop(0)
    print(sum(diff))
