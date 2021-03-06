from sys import stdin
stdin = open("bj-study/input.txt","r")

N,K=map(int,stdin.readline().split())
multi_tap=[0]*N
schedule = list(map(int,stdin.readline().split()))
temp=[]
for i in range(N):
    multi_tap[i]=schedule[i]
cnt=0
for i in range(N,K):
    if schedule[i] not in multi_tap:
        temp.append(schedule[i])
    if len(temp)!=0 and i%N==0:
        print(temp)
        for n in range(len(temp)):
            cnt+=1
            multi_tap[n]=temp.pop(0)
print(cnt)

