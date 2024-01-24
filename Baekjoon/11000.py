import sys
input = sys.stdin.readline
import heapq

N = int(input())
time = list()
for _ in range(N):
    time.append(tuple(map(int, input().split())))
time.sort()

classroom = list()
for start, end in time:
    if len(classroom) == 0:
        heapq.heappush(classroom, end)
    else:
        if start >= classroom[0]:
            heapq.heappop(classroom)
            heapq.heappush(classroom, end)
        else:
            heapq.heappush(classroom, end)

print(len(classroom))
