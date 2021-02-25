import math
cnt=0
def sol(n):
    global cnt
    k=math.sqrt(n)
    if n==0: 
        return cnt
    if k==int(k): # 제곱수 이면
        cnt+=1
        return sol(0)
    else:
        cnt+=1
        return sol(n-int(k)**2)
print(sol(int(input())))