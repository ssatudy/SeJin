'''
겹치는 구간을 병합
출력 : [[1,6],[8,10],[15,18]]
'''

arr = [[1,3], [2, 6], [8,10], [15,18]]
lst = []
ans = []
i = 0
while i < len(arr):
    if i == len(arr)-1:
        ans.append(arr[i])
        break

    if arr[i][1] >= arr[i+1][0]:
        lst = [arr[i][0], arr[i+1][1]]
        ans.append(lst)
        i += 1
    else:
        ans.append(arr[i])
    i += 1
print(ans)