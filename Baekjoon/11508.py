n = int(input())

c = list()
for _ in range(n):
    c.append(int(input()))
c.sort(reverse=True)

price = 0
for i in range(n):
    if i % 3 != 2:
        price += c[i]
print(price)
