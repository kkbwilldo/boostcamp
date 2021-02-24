#1
import sys
sys.setrecursionlimit(10**4)
def solution(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = (solution(n-1) + 2*solution(n-2))%10007
        return dp[n]


n = int(input())
dp = [0, 1, 3] + [0] * n
print(solution(n))




