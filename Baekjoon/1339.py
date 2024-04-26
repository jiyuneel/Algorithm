import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

alpha = dict()
for _ in range(N):
    word = input().strip()
    l = len(word)
    for i in range(l):
        if word[i] not in set(alpha.keys()):
            alpha[word[i]] = 0
        alpha[word[i]] += 10 ** (l - i - 1)

alpha = sorted(alpha.items(), key=lambda item: -item[1])

res = 0
num = deque(x for x in range(10))
for _, n in alpha:
    if n > 0:
        res += n * num.pop()
print(res)
