import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = deque([False] * N)

cnt = 0

while True:

    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    A.rotate(1)
    robot.rotate(1)

    # 로봇이 내리는 위치에 도달하면 즉시 내린다.
    robot[N - 1] = False

    # 벨트의 가장 오른쪽 로봇부터, 벨트가 회전하는 방향으로
    for i in range(N - 2, -1, -1):

        # 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있으면 로봇을 이동한다.
        if robot[i] and robot[i + 1] == False and A[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            A[i + 1] -= 1
            if A[i + 1] == 0:
                K -= 1

    # 로봇이 내리는 위치에 도달하면 즉시 내린다.
    robot[N - 1] = False

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if A[0] > 0:
        robot[0] = True
        A[0] -= 1
        if A[0] == 0:
            K -= 1

    cnt += 1

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if (K <= 0):
        break

print(cnt)
