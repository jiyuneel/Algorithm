import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num.sort()

res = 0
for i in range(N):
    l, r = 0, N - 1

    while True:
        if l == i:
            l += 1
        elif r == i:
            r -= 1

        if l >= r:
            break

        tmp = num[l] + num[r]
        if tmp == num[i]:
            res += 1
            break
        elif tmp < num[i]:
            l += 1
        elif tmp > num[i]:
            r -= 1
print(res)
