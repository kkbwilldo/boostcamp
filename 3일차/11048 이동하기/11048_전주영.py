from sys import stdin
#input -> sys.stdin.readline()
# stdin = open("input.txt", "r")
m,n=map(int,stdin.readline().split())
mat = [[0]*n for _ in range(m)]
# def pprint():
#     for _ in mat:
#         print(_)
#     print()

#make mat 입력값으로 초기화
for i in range(m): 
    for j,v in enumerate(map(int,stdin.readline().split())):
        mat[i][j]=v
# pprint()

for i in range(1,m):  #0 열 채우기
    mat[i][0]=mat[i-1][0]+mat[i][0]
for j in range(1,n):  #0 행 채우기
    mat[0][j]=mat[0][j-1]+mat[0][j]
# pprint()

for i in range(1,m):
    for j in range(1,n):
        mat[i][j]=mat[i][j]+max(mat[i-1][j-1],mat[i-1][j],mat[i][j-1])
# pprint()
print(mat[m-1][n-1])
    
