N, M = map(int, input().split())
card = list(map(int, input().split()))
visited = [0] * N
S = []
result = []
def back(k):
    if len(S) == 3:
        result.append(sum(S))
        return
    for i in range(k,N):
        if visited[i] == 0:
            visited[i] = 1
            S.append(card[i])
            back(i+1)
            visited[i] = 0
            S.pop()
back(0)

com = 99999999
idx = 0
for i in range(len(result)):
    a = M - result[i]
    if a >= 0 and a <= com:
        com = a
        idx = i

print(result[idx])


