import sys
input=sys.stdin.readline

n = int(input())
extension = dict()
for _ in range(n):
    file = input().strip()
    e = file.split('.')[1]
    if e not in extension.keys():
        extension[e] = 1
    else:
        extension[e] += 1
extension = sorted(extension.items())

for e, n in extension:
    print(e, n)
