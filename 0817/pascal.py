t = int(input())

for tc in range(1,t+1):
    n = int(input())

    arr = [[1] * X for X in range(1, n+1)]

    for i in range(1, n-1):
        for j in range(len(arr[i])-1):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
    print(f'#{tc}')
    for p in arr:
        print(*p)

