from sys import stdin

N = int(stdin.readline())
dp = [0] * 10000001
dp[1] = 1
dp[2] = 2
num = 3

while num < N+1:
    dp[num] = (dp[num-1] + dp[num-2]) % 15746
    num += 1

print(dp[N])