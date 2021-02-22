# https://www.acmicpc.net/problem/1010
def combi(m,n):
    a,b=1,1
    for x in range(n):
        a*= m-x
    for y in range(n):
        b*= y+1
    return a//b
    
from sys import stdin
#input -> sys.stdin.readline()
stdin = open("..\input.txt", "r")
T=int(stdin.readline())
for t in range(T):
    n,m = map(int,stdin.readline().split())
    print(combi(m,n))
