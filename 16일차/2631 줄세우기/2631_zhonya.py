from sys import stdin
#stdin = open("input.txt","r")
N=int(stdin.readline())
input_list=[int(stdin.readline()) for _ in range(N)]
dp=[1]*N
for idx,var in enumerate(input_list):
    if idx>0:
        for j in range(0,idx):
            if input_list[j]<var and dp[j]>=dp[idx]:
                dp[idx]=dp[j]+1
print(N-max(dp))
