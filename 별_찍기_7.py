N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    print('*'* (2*i-1))

for i in reversed(range(1, N)):
    print(' ' * (N - i), end='')
    print('*' * (2*i-1))
# https://www.acmicpc.net/problem/2444
