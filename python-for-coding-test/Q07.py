N = input().strip()
length = len(N)
left, right = 0, 0

for i in range(length // 2):
    left += int(N[i])
for i in range(length // 2, length):
    right += int(N[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
