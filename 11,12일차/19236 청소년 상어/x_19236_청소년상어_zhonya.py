from sys import stdin
stdin = open("input.txt","r")
mat=[[0]*4 for _ in range(4)]
for i in range(4):
    line = list(map(int,stdin.readline().split()))
    for j in range(4):
        t=[0,2,4,6]   
        mat[i][j]=[line[t[j]],line[t[j]+1]]
def pprint(mat):
    for _ in mat:
        print(_)
    print()

def eat(i,j):
    global score
    a,b=mat[i][j]
    score+=a
    mat[i][j]=["상",b]


def find_fish_idx(mat):
    index={}
    for i in range(4):
        for j in range(4):
            if mat[i][j][0]!=0:
                index[mat[i][j][0]]=[i,j]
    return index
def fish_suffle():
    for i in range(1,16+1):
        if i in fish_idx.keys():
            a,b=fish_idx[i]
            Dir=mat[a][b][1]
            while(True):
                #print("i:",i,"Dir:",Dir)
                a_=a+dy[Dir]
                b_=b+dx[Dir]
                if 0<=a_<4 and 0<=b_<4 and mat[a_][b_][0]!="상":
                    num=mat[a_][b_][0]
                    mat[a][b],mat[a_][b_]=mat[a_][b_],mat[a][b]
                    temp=fish_idx[num][:]
                    fish_idx[num]=fish_idx[i][:]
                    fish_idx[i] = temp
                    break
                else:
                    Dir+=1
                    if Dir>8: Dir=1
if __name__ == "__main__":
    score=0
    eat(0,0)
    pprint(mat)
    fish_idx=find_fish_idx(mat)
    print(fish_idx)
    print()
    dy=[0,-1,-1, 0, 1, 1, 1, 0,-1]
    dx=[0, 0,-1,-1,-1, 0, 1, 1, 1]
    fish_suffle()
    pprint(mat)
    eat_list=[]
    y,x=fish_idx["상"]
    Dir=mat[y][x][1]
    y+=dy[Dir]
    x+=dx[Dir]
    if 0<=x<4 and 0<=y<4:
        eat_list.append([y,x])