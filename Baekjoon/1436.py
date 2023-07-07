N = int(input())
num, cnt = 666, 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
