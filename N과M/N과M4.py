def dfs(start):
    if len(S) == M:
        print(' '.join(map(str, S)))
        return

    for i in range(start, N + 1):
        S.append(i)
        dfs(i)
        S.pop()

N, M = map(int, input().split())
S = []
dfs(1)