arr = [list(map(str, input().split())) for _ in range(5)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []
def back(r, c, idx, number):
    number += arr[r][c]
    if idx == 5:
        result.append(number)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5:
            back(nr, nc, idx+1, number)

for r in range(5):
    for c in range(5):
        back(r,c,0,'')

ans = set(result)
print(len(ans))