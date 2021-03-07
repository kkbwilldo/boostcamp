from sys import stdin
stdin=open("input.txt","r")
n=int(stdin.readline())

def m2d(input_list):
    t1,t2,t3,t4=input_list
    temp1=t1*100+t2
    temp2=t3*100+t4
    return [temp1,temp2]
flowers=[]
for _ in range(n):
    flowers.append(m2d(map(int,stdin.readline().split())))
start,end = m2d([3,1,11,30])
flowers.sort(key=lambda x:x[0])
cnt=0
save_p = 0
while(start<=end): #종료 조건
    if cnt>n: #무한 루프 방지 11월 30일 보다 작을경우
        cnt=0
        break
    temp=[]
    for i in range(save_p,n): #start 보다 작은 날짜 인덱스 찾기
        if flowers[i][0]<=start:
            temp.append(i)
        else:
            save_p=i
            break
    for j in temp: #위에서 찾은 인덱스 중 가장 end가 큰 꽃 선택.
        start=max(start,flowers[j][1])
    cnt+=1
print(cnt)