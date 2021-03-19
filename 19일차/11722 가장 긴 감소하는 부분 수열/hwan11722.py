from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())

num_arr = list(map(int, stdin.readline().split()))

answer = []

for i in range(len(num_arr)):
    num = num_arr[i] * -1

    if not answer or answer[-1] < num:
        answer += [num]
    
    else:
        answer[bisect_left(answer,num)] = num

print(len(answer))