import sys
input = sys.stdin.readline
from collections import deque

s1 = input().strip()
s2 = input().strip()
s2_l = len(s2)

res, tmp = deque(), deque()
for c in s1:
    res.append(c)

    i = s2_l - 1
    while res and i >= 0 and res[-1] == s2[i]:
        tmp.appendleft(res.pop())
        i -= 1
    if i >= 0:
        res.extend(tmp)
    tmp.clear()

if not res:
    print('FRULA')
else:
    print(''.join(res))
