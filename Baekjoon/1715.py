import sys
input = sys.stdin.readline
import heapq

N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))

res = 0
for _ in range(N - 1):
    a, b = heapq.heappop(card), heapq.heappop(card)
    res += a + b
    heapq.heappush(card, a + b)

print(res)
