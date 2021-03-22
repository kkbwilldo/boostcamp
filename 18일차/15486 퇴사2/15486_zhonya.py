from sys import stdin
stdin = open("input.txt","r")
N = int(stdin.readline())
Ti=[]
Pi=[]
# 시간 초과 미해결 , 퇴사 1 문제는 통과함.
for _ in range(N):
    t,p = map(int,stdin.readline().split())
    Ti.append(t)
    Pi.append(p)
dp=[0]*N

for i in range(N):
    # i번째 상담이 7일 안에 끝나고 i
    if i+Ti[i]<=N:
        dp[i]+=Pi[i]
        if i>0:
            temp=0 
            for j in range(0,i):
                if j+Ti[j]<=i: #상담일이 안겹쳐야
                    temp=max(temp,dp[j])
            dp[i]+=temp
print(Ti)
print(Pi)
print(dp)
print(max(dp))