import sys
input=sys.stdin.readline

N = int(input())
ans = list()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                ans.append(str(i) + str(j) + str(k))

for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = str(num)
    for n in ans[:]:
        s, b = 0, 0
        for i in range(3):
            if num[i] in n:
                if num[i] == n[i]: s += 1
                else: b += 1
        if not (s == strike and b == ball):
            ans.remove(n)
print(len(ans))
