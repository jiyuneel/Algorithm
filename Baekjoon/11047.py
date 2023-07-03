n, k = map(int, input().split())

value = []
for _ in range(n):
	value.append(int(input()))
value.reverse()

cnt = 0
for v in value:
	cnt += k // v
	k %= v

print(cnt)
