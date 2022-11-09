L = int(input())

for _ in range(L):
    left = []
    right = []
    pwd = input()

    for i in pwd:
        if i == '>':
            if right:
                left.append(right.pop())
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    final = reversed(right)
    print(''.join(left) + ''.join(final))