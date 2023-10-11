S = input().strip()
alpha = []
num = 0
for x in S:
    if x.isalpha():
        alpha.append(x)
    else:
        num += int(x)
alpha.sort()

print(''.join(alpha) + str(num))
