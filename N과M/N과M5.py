N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
visited = [0] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            out.append(lst[i])
            solve(depth+1, N, M)
            out.pop()
            visited[i] = 0

solve(0, N, M)