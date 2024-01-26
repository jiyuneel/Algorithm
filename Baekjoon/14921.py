import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left, right = 0, N - 1
res = A[0] + A[N - 1]

while left < right:
    tmp = A[left] + A[right]
    if abs(res) > abs(tmp):
        res = tmp

    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        break

print(res)
