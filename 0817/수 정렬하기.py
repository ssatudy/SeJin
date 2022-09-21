import sys

n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]


for i in range(len(arr)):
    n = len(arr)
    for j in range(1, n):
        if arr[j-1] >= arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
print(*arr, sep='\n')

