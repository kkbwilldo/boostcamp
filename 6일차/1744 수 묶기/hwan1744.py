from sys import stdin
from bisect import bisect_left, bisect_right

N = int(stdin.readline())
num_arr = []

for _ in range(N):
    num_arr.append(int(stdin.readline()))

num_arr.sort()
zero_idx = bisect_right(num_arr, 0)
one_idx = bisect_right(num_arr, 1)
answer = 0


if zero_idx % 2 == 0:
    for i in range(0, zero_idx, 2):
        answer += num_arr[i] * num_arr[i+1]


else:
    for i in range(0, zero_idx-1, 2):
        answer += num_arr[i] * num_arr[i+1]
    answer += num_arr[zero_idx-1]
    

if one_idx == len(num_arr):
    pass

elif (len(num_arr) - one_idx) % 2 == 0:
    for i in range(len(num_arr)-1, one_idx, -2):
        answer += num_arr[i] * num_arr[i-1]
else:
    for i in range(len(num_arr)-1, one_idx+1, -2):
        answer += num_arr[i] * num_arr[i-1]
    answer += num_arr[one_idx]


for i in range(zero_idx, one_idx):
    answer += num_arr[i]


print(answer)