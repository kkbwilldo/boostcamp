from sys import stdin,maxsize
stdin = open("input.txt","r")
n = int(stdin.readline())
dist = list(map(int,stdin.readline().split()))
oil = list(map(int,stdin.readline().split()))
cost = 0 
Min=maxsize
for i in range(0,n-1):
    if i==0:
        cost += oil[i]*dist[i]
        Min = min(Min,oil[i])
    else:
        Min = min(Min,oil[i])
        cost += Min * dist[i]
print(cost)
