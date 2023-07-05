n = int(input())
len = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost, price = 0, oil[0]
for i in range(n - 1):
    cost += price * len[i]
    if price > oil[i + 1]:
        price = oil[i + 1]
print(cost)
