import sys
input = sys.stdin.readline

N = int(input())
studentNum = list()
studentLike = list()
studentDict = dict()

for _ in range(N * N):
    info = list(map(int, input().split()))
    studentNum.append(info[0])
    studentLike.append(info[1:])
    studentDict[info[0]] = info[1:]

classroom = [[0 for _ in range(N)] for _ in range(N)]

for num in range(N * N):
    row, col = 0, 0
    likeCount, emptyCount = -1, -1

    for i in range(N):
        for j in range(N):

            if classroom[i][j] != 0:
                continue

            tmpLikeCount, tmpEmptyCount = 0, 0
            if i != 0:
                if classroom[i - 1][j] == 0:
                    tmpEmptyCount += 1
                elif classroom[i - 1][j] in studentLike[num]:
                    tmpLikeCount += 1
            if i != N - 1:
                if classroom[i + 1][j] == 0:
                    tmpEmptyCount += 1
                elif classroom[i + 1][j] in studentLike[num]:
                    tmpLikeCount += 1
            if j != 0:
                if classroom[i][j - 1] == 0:
                    tmpEmptyCount += 1
                elif classroom[i][j - 1] in studentLike[num]:
                    tmpLikeCount += 1
            if j != N - 1:
                if classroom[i][j + 1] == 0:
                    tmpEmptyCount += 1
                elif classroom[i][j + 1] in studentLike[num]:
                    tmpLikeCount += 1

            if tmpLikeCount > likeCount:
                likeCount = tmpLikeCount
                emptyCount = tmpEmptyCount
                row, col = i, j
            elif tmpLikeCount == likeCount and tmpEmptyCount > emptyCount:
                likeCount = tmpLikeCount
                emptyCount = tmpEmptyCount
                row, col = i, j
            
    classroom[row][col] = studentNum[num]

score = 0
for i in range(N):
    for j in range(N):
        cnt = 0

        if i != 0 and classroom[i - 1][j] in studentDict[classroom[i][j]]:
            cnt += 1
        if i != N - 1 and classroom[i + 1][j] in studentDict[classroom[i][j]]:
            cnt += 1
        if j != 0 and classroom[i][j - 1] in studentDict[classroom[i][j]]:
            cnt += 1
        if j != N - 1 and classroom[i][j + 1] in studentDict[classroom[i][j]]:
            cnt += 1

        if cnt == 4:
            score += 1000
        elif cnt == 3:
            score += 100
        elif cnt == 2:
            score += 10
        elif cnt == 1:
            score += 1

print(score)
