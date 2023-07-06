s = list(input())
i = 0
while i < len(s):
    if s[i] == '<':
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():
        j = i
        while i < len(s) and s[i].isalnum():
            i += 1
        s[j:i] = reversed(s[j:i])
    else:
        i += 1
print(''.join(s))
