n, m = map(int, input().split())
board = list()
for _ in range(n):
    board.append(input())

cnt = 0
for i in range(n - 7):
    for j in range(m - 7):
        chess = [board[x][j:j + 8] for x in range(i, i + 8)]
        black, white = 0, 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if chess[x][y] == 'B': white += 1
                    elif chess[x][y] == 'W': black += 1
                else:
                    if chess[x][y] == 'B': black += 1
                    elif chess[x][y] == 'W': white += 1
        cnt = min(cnt, black, white) if i + j else min(black, white)
print(cnt)
