import sys
input = sys.stdin.readline
import heapq

N = int(input())
meeting = list()
for _ in range(N):
    meeting.append(tuple(map(int, input().split())))
meeting.sort()

room = [meeting[0][1]]
res, cnt = 1, 1
for i in range(1, N):
    heapq.heappush(room, meeting[i][1])
    if meeting[i][0] < room[0]:
        cnt += 1
        res = max(res, cnt)
    else:
        heapq.heappop(room)
print(res)
