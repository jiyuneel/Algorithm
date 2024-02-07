import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0] * 6

command = list(map(int, input().split()))

def rotate_east(dice):
    new_dice = dice[:]
    new_dice[0] = dice[3]
    new_dice[2] = dice[0]
    new_dice[3] = dice[5]
    new_dice[5] = dice[2]
    return new_dice

def rotate_west(dice):
    new_dice = dice[:]
    new_dice[0] = dice[2]
    new_dice[2] = dice[5]
    new_dice[3] = dice[0]
    new_dice[5] = dice[3]
    return new_dice

def rotate_north(dice):
    new_dice = dice[:]
    new_dice[0] = dice[4]
    new_dice[1] = dice[0]
    new_dice[4] = dice[5]
    new_dice[5] = dice[1]
    return new_dice

def rotate_south(dice):
    new_dice = dice[:]
    new_dice[0] = dice[1]
    new_dice[1] = dice[5]
    new_dice[4] = dice[0]
    new_dice[5] = dice[4]
    return new_dice

for cmd in command:
    nx = x + dx[cmd - 1]
    ny = y + dy[cmd - 1]

    if not(0 <= nx < N and 0 <= ny < M):
        continue

    if cmd == 1:
        dice = rotate_east(dice)
    elif cmd == 2:
        dice = rotate_west(dice)
    elif cmd == 3:
        dice = rotate_north(dice)
    elif cmd == 4:
        dice = rotate_south(dice)
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])
    x, y = nx, ny

'''
[1 2 3 4 5 6]
  2
4 1 3
  5
  6

동
[4 2 1 6 5 3]
  2
6 4 1
  5
  3

서
[3 2 6 1 5 4]
  2
1 3 6
  5
  4

북
[5 1 3 4 6 2]
  1
4 5 3
  6
  2

남
[2 6 3 4 1 5]
  6
4 2 3
  1
  5
'''
