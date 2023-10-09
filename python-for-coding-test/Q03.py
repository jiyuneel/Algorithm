str = input()
cnt0 = 0
cnt1 = 0

if str[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

for i in range(1, len(str)):
    if  str[i] != str[i - 1]:
        if str[i] == '0':
            cnt1 += 1
        else:
            cnt0 += 1

print(min(cnt0, cnt1))
