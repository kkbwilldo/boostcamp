from sys import stdin
stdin = open("bj-study/input.txt","r")

def sol(n,m):
    chess=[[0]*m for _ in range(n)]
    chess[n-1][0]=1
    for 

    for c in chess:
        print(c)
#이전에 방문 x
#체스판 안이면 이동

n,m = map(int,stdin.readline().split())
sol(2,4)