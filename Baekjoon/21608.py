import sys
input = sys.stdin.readline

N = int(input())
student = list()
studentDict = dict()
seat = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N * N):
    info = list(map(int, input().split()))
    student.append(info)
    studentDict[info[0]] = info[1:]

for num in range(N * N):
    row, col = 0, 0
    maxLike, maxEmpty = -1, -1

    for i in range(N):
        for j in range(N):
            if seat[i][j] != 0:
                continue

            tmpLike, tmpEmpty = 0, 0
            for d in range(4):
                x = j + dx[d]
                y = i + dy[d]

                if 0 <= x < N and 0 <= y < N:
                    if seat[y][x] == 0:
                        tmpEmpty += 1
                    elif seat[y][x] in student[num][1:]:
                        tmpLike += 1

            if tmpLike > maxLike:
                maxLike, maxEmpty = tmpLike, tmpEmpty
                row, col = i, j
            elif tmpLike == maxLike and tmpEmpty > maxEmpty:
                maxLike, maxEmpty = tmpLike, tmpEmpty
                row, col = i, j

    seat[row][col] = student[num][0]

score = 0
for i in range(N):
    for j in range(N):
        cnt = 0

        for d in range(4):
            x = j + dx[d]
            y = i + dy[d]
            if 0 <= x < N and 0 <= y < N:
                if seat[y][x] in studentDict[seat[i][j]]:
                    cnt += 1

        if cnt > 0:
            score += 10 ** (cnt - 1)

print(score)
