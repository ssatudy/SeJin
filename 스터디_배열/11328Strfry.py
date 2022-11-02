N = int(input())

for i in range(N):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    print('Possible' if a == b else 'Impossible')
