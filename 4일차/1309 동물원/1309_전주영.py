n=int(input())

dp=[[0,0,0] for _ in range(n+1)]
#dp[i][0] -> 사자 배치 x
#dp[i][1] -> 사자 왼쪽 배치
#dp[i][2] -> 사자 오른쪽 배치
for k in range(3):
    dp[1][k]=1
for x in range(2,n+1):
    dp[x][0] = (dp[x-1][0] + dp[x-1][1] + dp[x-1][2]) % 9901 #이번 순서에 빈칸인 경우는 위의 모든 케이스에 가능
    dp[x][1] = (dp[x-1][0] + dp[x-1][2]) % 9901 #이번 순서에 왼쪽에 놓으려면 이전 순서에 오른쪽인 경우 + 빈칸인 경우
    dp[x][2] = (dp[x-1][0] + dp[x-1][1]) % 9901 #이번 순서에 오른쪽에 놓으려면 이전 순서에 왼쪽인 경우 + 빈칸인 경우
# for x in range(n+1):
#     print(dp[x])
print(sum(dp[n]) % 9901)
