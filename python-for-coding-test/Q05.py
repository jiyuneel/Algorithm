N, M = map(int, input().split())
ball = list(map(int, input().split()))

weight = [0] * (M + 1)
for b in ball:
    weight[b] += 1

# res = 0
# for i in range(M):
#     for j in range(i + 1, M):
#         if weight[i] != 0 and weight[j] != 0:
#             res += weight[i] * weight[j]
res = 0
for i in range(M):
    N -= weight[i]
    res += weight[i] * N

print(res)
