import sys
input = sys.stdin.readline

N = int(input())
color = input().strip()

red = 1 if color[0] == 'R' else 0
blue = 1 if color[0] == 'B' else 0

res = 0
for i in range(1, N):
    if color[i] != color[i - 1]:
        res += 1
        if color[i] == 'R':
            red += 1
        elif color[i] == 'B':
            blue += 1

print(min(red, blue) + 1)
