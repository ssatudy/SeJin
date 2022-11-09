word = list(map(str,input().rstrip()))
stack = []
N = len(word)
M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == 'L'and word:
        stack.append(word.pop())
    elif command[0] == 'D' and stack:
        word.append(stack.pop())
    elif command[0] == 'B' and word:
        word.pop()
    elif command[0] == 'P':
        word.append(command[1])

final = list(reversed(stack))

print(''.join(word + final))