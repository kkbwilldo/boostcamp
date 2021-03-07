# 틀린 케이스 -> 그리디로 풀이함. 18? 에서 반례
# import math
# cnt=0
# def sol(n):
#     global cnt
#     k=math.sqrt(n)
#     if n==0: 
#         return cnt
#     if k==int(k): # 제곱수 이면
#         cnt+=1
#         return sol(0)
#     else:
#         cnt+=1
#         return sol(n-int(k)**2)
# print(sol(int(input())))
n=int(input())
dp=[0]*(n+1) #0~n
import math
for i in range(1,n+1):
    dp[i]=i
    for j in range(int(math.sqrt(i))+1):
        dp[i]=min(dp[i],dp[i-j**2]+1)
print(dp[n])