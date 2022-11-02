N, K = map(int,input().split())
grade = [0] * 7
gl = []
arr = [list(map(int,input().split())) for _ in range(N)]

Fe = []
Ma = []
Fer = [0] * 7
Mar = [0] * 7
for i in range(len(arr)):
    if arr[i][0] == 0:
        Fe.append(arr[i][1])

    else:
        Ma.append(arr[i][1])


for n in Fe:
    Fer[n] += 1
for m in Ma:
    Mar[m] += 1

cnt = 0
for _ in range(1001):
    for f in range(1,7):
        if Fer[f] > K:
            Fer[f] -= K
            cnt += 1
    for l in range(1,7):
        if Mar[l] > K:
            Mar[l] -= K
            cnt += 1

for s in range(1,7):
    if Fer[s] <= K and Fer[s] != 0:
        cnt += 1
    if Mar[s] <= K and Mar[s] != 0:
        cnt += 1

print(cnt)