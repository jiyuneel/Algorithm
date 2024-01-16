N = int(input())
fear = list(map(int, input().split()))

fear.sort()
group, cnt = 0, 0

for f in fear:
    cnt += 1
    if cnt >= f:
        group += 1
        cnt = 0

print(group)
