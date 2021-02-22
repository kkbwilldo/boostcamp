#https://www.acmicpc.net/problem/11727
N=int(input())
dp=[0 for x in range(N+1)]
result=0
for n in range(N+1):
    if n==1:
        dp[n]=1
    if n==2:
        dp[n]=3
    if n==3:
        dp[n]=5
    if n>3:
        dp[n]=dp[n-1]+2*dp[n-2]
print(dp[N]%10007)


