paren = input()
stack = []
cnt = 0

for i in range(len(paren)):
    if paren[i] == '(':
        stack.append(paren[i])

    elif paren[i] == ')':
        stack.pop()
        if paren[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
