N = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for n in coin:
    if target < n:
        break
    target += n
print(target)
