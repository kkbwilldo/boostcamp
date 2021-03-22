from sys import stdin
stdin = open("input.txt","r")
N = int(stdin.readline())
List = list(map(int,stdin.readline().split()))
dp=[1]*N
print(dp)
print(List)
for i in range(N):
    for j in range(0,i+1):
        if List[j]>List[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)
print(max(dp))