import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = list()
for _ in range(R):
    board.append(list(input().strip()))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res, cnt = 1, 0
check = [False] * 26

def dfs(x, y):
    global res, cnt
    check[ord(board[x][y]) - ord('A')] = True
    cnt += 1

    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < R and 0 <= yy < C and not check[ord(board[xx][yy]) - ord('A')]:
            dfs(xx, yy)
            res = max(res, cnt)
            check[ord(board[xx][yy]) - ord('A')] = False
            cnt -= 1

dfs(0, 0)
print(res)
