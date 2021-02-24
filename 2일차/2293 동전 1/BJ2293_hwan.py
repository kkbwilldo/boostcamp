from sys import stdin

n, k = map(int, stdin.readline().split())
coin_arr = [int(stdin.readline()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for i in coin_arr:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])