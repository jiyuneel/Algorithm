import sys
input = sys.stdin.readline

bingo, num = list(), list()
for _ in range(5):
    bingo.append(list(map(int, input().split())))
for _ in range(5):
    num.append(list(map(int, input().split())))
bingo, num = sum(bingo, []), sum(num, [])

def isBingo(b):
    cnt = 0
    if sum(b[:5]) == 0: cnt += 1
    if sum(b[6:10]) == 0: cnt += 1
    if sum(b[11:15]) == 0: cnt += 1
    if sum(b[16:20]) == 0: cnt += 1
    if sum(b[21:]) == 0: cnt += 1

    if sum(b[::5]) == 0: cnt += 1
    if sum(b[1::5]) == 0: cnt += 1
    if sum(b[2::5]) == 0: cnt += 1
    if sum(b[3::5]) == 0: cnt += 1
    if sum(b[4::5]) == 0: cnt += 1

    if sum(b[::6]) == 0: cnt += 1
    if sum(b[4:21:4]) == 0: cnt += 1

    return True if cnt >= 3 else False


for i in range(25):
    bingo[bingo.index(num[i])] = 0
    if isBingo(bingo):
        print(i + 1)
        break
