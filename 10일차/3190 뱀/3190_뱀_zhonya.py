from sys import stdin
from collections import deque
stdin=open("input.txt","r")
N=int(stdin.readline())
K=int(stdin.readline())
mat = [[0]*N for _ in range(N)]
def pprint(mat):
    for m in mat:
        print(m)
    print()
for _ in range(K):
    a,b =map(int,stdin.readline().split())
    mat[a-1][b-1]=4 #사과
L = int(stdin.readline())
i,j=0,0
mat[i][j]=1 #뱀은 0,0위치 시작
cnt=1
track=deque([[0,0]])
dir_change=dict()
dir_=0 # 0 : 우, 1 : 하, 2:좌 , 3: 상
dy=[0,1,0,-1]
dx=[1,0,-1,0]
for _ in range(L):
    X,C = stdin.readline().split()
    X=int(X)
    C=str(C)
    dir_change[X]=C
while(True):
    i,j=i+dy[dir_],j+dx[dir_]
    if 0<=i<N and 0<=j<N and mat[i][j]!=1:
        if mat[i][j]!=4: #없으면 머리늘리고 꼬리 줄이고
            tale_i,tale_j=track.popleft()
            mat[tale_i][tale_j]=0
        mat[i][j]=1
        track.append([i,j])
        if cnt in dir_change.keys():
            if dir_change[cnt]=="L":
                dir_ = (dir_ - 1) % 4
            elif dir_change[cnt]=="D":
                dir_ = (dir_ + 1) % 4
        cnt+=1
    else: #범위 바깥 이거나 자신을 만남
        break
print(cnt)