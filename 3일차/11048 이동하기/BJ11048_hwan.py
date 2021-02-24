from sys import stdin

N, M = map(int, stdin.readline().split())

dp = [[0] * (M+1)]
for i in range(N):
    dp.append([0] + list(map(int, stdin.readline().split())))

for i in range(1,N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j]+dp[i][j], dp[i][j-1]+dp[i][j])

print(dp[N][M])