from sys import stdin
stdin = open("input.txt","r")
N = int(stdin.readline())
List = list(map(int,stdin.readline().split()))
dp=List[:]

for i in range(N):
    for j in range(0,i+1):
        if List[j]<List[i]:
            dp[i]=max(dp[j]+List[i],dp[i])
print(dp)
print(max(dp))