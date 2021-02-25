from sys import stdin

T = int(stdin.readline())
for tc in range(T):
    K = int(stdin.readline())
    num_array = list(map(int, stdin.readline()))

    while K > 1:
        temp = 