calc = input().split('-')
for i in range(len(calc)):
    if '+' in calc[i]:
        num = list(map(int, calc[i].split('+')))
        calc[i] = sum(num)

res = int(calc[0])
for i in range(1, len(calc)):
    res -= int(calc[i])
print(res)
