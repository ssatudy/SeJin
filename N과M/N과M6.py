N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
visited = [0] * N
out = []

def solve(d, idx, N, M):
    if d == M:    # 깊이로 파악
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            out.append(lst[i])
            solve(d+1, i+1, N, M)
            out.pop()
            visited[i] = 0

solve(0, 0, N, M)