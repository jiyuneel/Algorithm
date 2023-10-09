num = input()
res = 0

for n in num:
    if res <= 1 or n == '0' or n == '1':
        res += int(n)
    else:
        res *= int(n)

print(res)
