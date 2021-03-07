from sys import stdin
stdin = open("input.txt","r")
R,C = map(int,stdin.readline().split())
mat = [list("x"*(C+2))]
mat += [list("x"+stdin.readline()[:-1]+"x") for _ in range(R-1)]
mat.append(list("x"+stdin.readline()+"x"))
mat.append(list("x"*(C+2)))
visited=[[False]*(C+2) for _ in range(R+2)]

def pprint(list_):
    for _ in list_:
        print(_)
    print()


def dfs(y,x):
    if x == C:
        return True
    for d in dx:
        if mat[y+d][x+1] =="." and not visited[y+d][x+1]:
            visited[y+d][x+1]=True
            if dfs(y+d,x+1):
                return True
    return False

dx = [-1, 0, 1]
ans = 0
for i in range(1,R+1):
    if mat[i][1] == '.':
        if dfs(i, 0):
            ans += 1
print(ans)


