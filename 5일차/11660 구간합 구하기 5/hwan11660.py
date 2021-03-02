from sys import stdin

N, M = map(int, stdin.readline().split())

dp =[[0]*(N+1)] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

find_sum = [list(map(int, stdin.readline().split())) for _ in range(M)]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for x1, y1, x2, y2 in find_sum:
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)