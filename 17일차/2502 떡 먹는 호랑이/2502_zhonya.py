from sys import stdin
stdin = open("input.txt","r")
D , K = map(int,stdin.readline().split())
a_list=[1,0]
b_list=[0,1]
def fibo(input_list): #최대 30개여서 미리 a와 b의 방정식 계수를 구해둠
    for i in range(2,29+1):
        input_list.append(input_list[i-1]+input_list[i-2])
    return input_list
a_list = fibo(a_list)
b_list = fibo(b_list)
#1<=a<=b
a=1
b=1
flag=True
ans=[]
while(flag): # 부르트 포스
    while(True):
        if a*a_list[D-1]+b*b_list[D-1] == K:
            flag=False
            ans.append(a)
            ans.append(b)
            break
        elif a*a_list[D-1]+b*b_list[D-1] > K:
            b=a
            break
        b+=1
    a+=1
print(ans[0])
print(ans[1])   