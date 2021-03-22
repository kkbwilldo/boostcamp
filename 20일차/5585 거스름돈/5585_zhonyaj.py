from sys import stdin
stdin = open("input.txt","r")
n = 1000 - int(stdin.readline())
cnt=0
for i in [500,100,50,10,5,1]:
    cnt+= n // i
    n = n % i
print(cnt)