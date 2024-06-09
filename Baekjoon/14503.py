import sys
input = sys.stdin.readline

n, m = map(int, input().split())
robot_r, robot_c, robot_d = map(int, input().split())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

room = list()
for _ in range(n):
    room.append(list(map(int, input().split())))

# 주변 4칸 중 청소되지 않은 빈 칸이 있으면 True, 없으면 False
def check_surrounding(row, col):
    if row > 0 and room[row - 1][col] == 0:
        return True
    if row < n - 1 and room[row + 1][col] == 0:
        return True
    if col > 0 and room[row][col - 1] == 0:
        return True
    if col < m - 1 and room[row][col + 1] == 0:
        return True
    return False

count = 0
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[robot_r][robot_c] == 0:
        room[robot_r][robot_c] = 2
        count += 1
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    elif not check_surrounding(robot_r, robot_c):
        back_r, back_c = robot_r + direction[robot_d][0] * -1, robot_c + direction[robot_d][1] * -1
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if room[back_r][back_c] != 1:
            robot_r, robot_c = back_r, back_c
            continue
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    elif check_surrounding(robot_r, robot_c):
        # 반시계 방향으로 90도 회전한다.
        robot_d = (robot_d - 1) % 4
        front_r, front_c = robot_r + direction[robot_d][0], robot_c + direction[robot_d][1]
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        if room[front_r][front_c] == 0:
            robot_r, robot_c = front_r, front_c
            continue

print(count)
