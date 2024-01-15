import sys
input = sys.stdin.readline

N = int(input())
honey = list(map(int, input().split()))
total = sum(honey)

# 왼쪽 끝에 벌 한 마리, 오른쪽 끝에 벌통을 둔 경우
case1 = 0
x = 0
for i in range(1, N):
    tmp = (total - honey[0] - honey[i]) * 2 - x
    x += honey[i]

    if tmp > case1:
        case1 = tmp

# 왼쪽 끝에 벌통, 오른쪽 끝에 벌 한 마리를 둔 경우
case2 = 0
honey.reverse()
x = 0
for i in range(1, N):
    tmp = (total - honey[0] - honey[i]) * 2 - x
    x += honey[i]

    if tmp > case2:
        case2 = tmp

# 양쪽 끝에 벌을 둔 경우
case3 = (total - honey[0] - honey[-1]) + max(honey[1:-1])

print(max(case1, case2, case3))
