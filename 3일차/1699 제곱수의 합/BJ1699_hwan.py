from sys import stdin
import math

N = int(stdin.readline())
dp = [0] * (N+1)


for i in range(1, N+1):
    dp[i] = i
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i - j**2]+1)

    
print(dp[-1])