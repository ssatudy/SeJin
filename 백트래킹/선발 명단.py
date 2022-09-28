T = int(input())


def back(k, s):
    global maxx
    if k == 11:
        if s > maxx:
            maxx = s
            return
    for i in range(11):
        if visited[i] == 0 and player[k][i] != 0:    # 0점의 선수는 포함하지 않아야 함
            visited[i] = 1
            s += player[k][i]
            back(k + 1, s)
            s -= player[k][i]
            visited[i] = 0

for tc in range(1, T+1):
    player = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    maxx = 0
    back(0,0)
    print(maxx)