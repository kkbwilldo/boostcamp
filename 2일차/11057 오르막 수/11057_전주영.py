n=int(input())
dp=[[0]*10 for x in range(n)]
dp[0] = [1 for i in range(10)]
for i in range(1,n):
    for j in range(9,-1,-1):
        if j == 9:
            dp[i][j] = sum(dp[i-1])
        else:
            dp[i][j] = dp[i][j+1]-dp[i-1][j+1]

# for d in dp:
#     print(d)

print(sum(dp[n-1])%10007)    

