from sys import stdin
stdin=open("input.txt","r")
n=int(stdin.readline())
k=int(stdin.readline())
sensor=set(map(int,stdin.readline().split())) #중복 제거
sensor=list(sensor)
sensor.sort() #오름차순 정렬해서 
dist=[] #차를 dist에 저장할 거다.
if len(sensor)>1:
    for i in range(len(sensor)-1):
        dist.append(sensor[i+1]-sensor[i])
    #기지국을 k개 설치하려면 거리 list 에서 k-1개를 최대값 순대로 제거
    for _ in range(k-1): 
        Max=max(dist)
        dist.remove(Max)
else: #센서가 1개 뿐인 경우는 길이 0 
    dist=[0]
print(sum(dist)) #남은 길이의 합
    
