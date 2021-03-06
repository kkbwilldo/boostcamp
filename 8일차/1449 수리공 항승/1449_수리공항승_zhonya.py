from sys import stdin
stdin = open("bj-study/input.txt","r")

N,L=map(int,stdin.readline().split())
pipe=[0]*1001
for x in map(int,stdin.readline().split()): #파이프에 구멍 표시
    pipe[x]=1

cnt=0
for idx,p in enumerate(pipe): 
    if p == 1: #구멍이면
        cnt+=1 
        for j in range(idx,idx+L):
            if j <1000:
                pipe[j]=2 #스티커 붙인다.
    elif p == 2: #이미 스티커이면 넘어간다.
        pass
print(cnt)
