from sys import stdin

N, M = map(int, stdin.readline().split())


if N >=3:
    if M >= 7:
        print(M-2)
    elif M >= 4:
        print(4)
    else:
        print(M)
elif N == 2:
    if M >= 7:
        print(4)
    else:
        print((M+1)//2)
else:
    print(1)
