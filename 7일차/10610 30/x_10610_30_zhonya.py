from sys import stdin
stdin = open("bj-study/input.txt","r")

def sol(num):
    num.sort(reverse=True)
    print(num)
    # for s in num:


for x in range(4):
    num=list(stdin.readline()[:-1])
    print(x+1,end=" ")
    sol(num)