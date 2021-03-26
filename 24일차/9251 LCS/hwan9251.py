from sys import stdin
from pprint import pprint

input_a = stdin.readline().rstrip()
input_b = stdin.readline().rstrip()

dp = [[0]*(len(input_a)+1) for _ in range(len(input_b)+1)]

for i in range(1,len(input_b)+1):
    for j in range(1, len(input_a)+1):
        temp = dp[i-1][j-1] + (input_a[j-1] == input_b[i-1])
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], temp)

# pprint(dp)
print(dp[-1][-1])