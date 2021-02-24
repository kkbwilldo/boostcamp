
from sys import stdin
# N=int(stdin.readline())
# table=list(map(int,stdin.readline().split()))
N=6
table=[10,20,10,30,20,50]
dp=[ 1 for x in range(N)]

for x in range(N):
    for y,val in enumerate(table[:x]):
        if val<table[x]:
            print(dp[x],dp[y]+1)
            dp[x]=max(dp[x],dp[y]+1)
print(max(dp))




