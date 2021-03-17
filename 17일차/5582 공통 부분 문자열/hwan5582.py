from sys import stdin
from pprint import pprint
from itertools import chain
input = stdin.readline


A_input = list(map(str, input().rstrip()))
B_input = list(map(str, input().rstrip()))

dp = [[0]*(len(A_input)+1) for _ in range((len(B_input)+1))]


for i in range(1,len(B_input)+1):
    for j in range(1,len(A_input)+1):
        
        if B_input[i-1] == A_input[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
# pprint(dp)
print(max(chain(*dp)))