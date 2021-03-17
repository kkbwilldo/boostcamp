from sys import stdin
input = stdin.readline
from bisect import bisect_left

N = int(input())
num_list = [int(input()) for _ in range(N)]
dp = [num_list[0]]

for i in range(1,N):
    
    if dp[-1] < num_list[i]:
        dp += [num_list[i]]
    
    else:
        dp[bisect_left(dp, num_list[i])] = num_list[i]
    
print(len(num_list) - len(dp))