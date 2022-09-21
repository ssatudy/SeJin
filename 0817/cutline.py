N , k = map(int, input().split())

arr = list(map(int,input().split()))

lst = []

for i in range(len(arr)):
    for j in range(1, N):
        if arr[j - 1] <= arr[j]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
print(arr[k-1])
