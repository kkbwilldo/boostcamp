from sys import stdin

N = int(stdin.readline())
dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [i for i in range(10, 0, -1)]

for i in range(2,N+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]
print(dp[N][0] % 10007)