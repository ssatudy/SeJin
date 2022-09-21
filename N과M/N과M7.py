N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
out = []

def solve(d, N, M):
    if d == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(lst[i])
        solve(d+1, N, M)
        out.pop()

solve(0, N, M)