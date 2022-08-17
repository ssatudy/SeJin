'''
입력 : 4->2->1->3
출력 : 1->2->3->4
'''

arr = [4, 2, 1, 3]

for i in range(len(arr)):
    n = len(arr) - 1
    for j in range(1, n):
        if arr[j-1] >= arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp

print(arr)



