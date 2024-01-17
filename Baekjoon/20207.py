import sys
input = sys.stdin.readline

N = int(input())
calendar = [0] * 366
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        calendar[i] += 1

sum = 0
width, height = 0, 0
for i in range(1, 366):
    if calendar[i] != 0:
        width += 1
        if calendar[i] > height:
            height = calendar[i]

    if calendar[i] == 0 or i == 365:
        sum += width * height
        width, height = 0, 0

print(sum)
