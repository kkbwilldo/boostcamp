from sys import stdin
from pprint import pprint
stdin = open("input.txt","r")
A = stdin.readline().rstrip()
B = stdin.readline().rstrip()

dp=[[0]*(len(A)+1) for _ in range(len(B)+1)]
Max=0
for i in range(1,len(B)+1):
    for j in range(1,len(A)+1):
        if A[j-1]==B[i-1]: #여기서 틀린거!!!!
            dp[i][j]=dp[i-1][j-1]+1
            Max=max(Max,dp[i][j])

pprint(dp)
print(Max)