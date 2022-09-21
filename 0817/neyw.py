t = int(input())
n = int(input())

for tc in range(t):
    arr = [[0] * (i + 1) for i in range(n)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

        # 한 줄씩 출력
    print(f'#{tc + 1}')
    for m in arr:
        print(*m)

    # print(f'#{tc+1}')
    # for lst in arr:
    #     result = [x for x in lst if x]
    #     print(*result)