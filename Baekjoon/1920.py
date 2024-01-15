N = int(input())
A = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

def binary_search(arr, start, end, num):
    if start > end:
        return 0

    mid = (start + end) // 2
    if num == arr[mid]:
        return 1
    elif num < arr[mid]:
        return binary_search(arr, start, mid - 1, num)
    else:
        return binary_search(arr, mid + 1, end, num)


A.sort()
for n in num:
    print(binary_search(A, 0, N - 1, n))
