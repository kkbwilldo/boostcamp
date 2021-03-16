from sys import stdin
stdin = open("input.txt","r")

n = int(stdin.readline())
mat = []
for _ in range(n):
    mat.append(list(map(int,stdin.readline().split())))

def pprint(mat):
    for _ in mat:
        print(_)

dy=[-1,1,0,0]
dx=[0,0,-1,1]
visited=[[False]*n for _ in range(4)]
pprint(mat)
print()
pprint(visited)

def dfs(i,j):
    for _ in range(4):
        cnt=1
        temp=mat[i][j]
        visited[i][j]=True
        i=i+dy[_]
        x=j+dx[_]
        if 0<=i<4 and 0<=j<4:
            if mat[i][j]>temp and visited[i][j]==False:
                cnt+=1
                return dfs(i,j)
            return cnt
if __name__ in "__main__":
    Max=1
    for i in range(n):
        for j in range(n):
            Max=max(Max,dfs(i,j))
    print(Max)