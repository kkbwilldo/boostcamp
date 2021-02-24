n = int(input())
dp = [1, 0, 3] + [0] * (n + 1)
for i in range(4, n + 1, 2):
    dp[i] = 4 * dp[i-2] - dp[i-4]

print(dp[n])