from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())

line = sorted([tuple(map(int, stdin.readline().split())) for _ in range(N)])
answer = [line[0][1]]

for a, b in line:
    if b > answer[-1]:
        answer.append(b)
    else:
        answer[bisect_left(answer, b)] = b
print(N - len(answer))