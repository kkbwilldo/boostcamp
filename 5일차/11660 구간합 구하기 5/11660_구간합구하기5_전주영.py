from sys import stdin
stdin = open("input.txt","r")
n,m= map(int,stdin.readline().split())
mat=[[0]+list(map(int,stdin.readline().split())) for _ in range(n)]
mat.insert(0,[0]*(n+1))

a=len(mat)
b=len(mat[0])
for i in range(1,a):
    for j in range(1,b):
        mat[i][j]+=mat[i-1][j]+mat[i][j-1]-mat[i-1][j-1]

for _ in range(m):
    y1,x1,y2,x2=list(map(int,stdin.readline().split()))
    result=mat[y2][x2]-mat[y2][x1-1]-mat[y1-1][x2]+mat[y1-1][x1-1]
    print(result)