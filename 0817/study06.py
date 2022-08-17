'''
색정렬 빨 - 0 / 흰 - 1 / 파 - 2
순서대로 정렬
'''
arr = [2,0,2,1,1,0]
# [0,0,1,1,2,2]


for i in range(len(arr)):
    n = len(arr)
    for j in range(1, n):
        if arr[j-1] >= arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
print(arr)