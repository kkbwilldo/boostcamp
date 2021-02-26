def combi(m,n):
    a,b=1,1
    for x in range(n):
        a*= m-x
    for y in range(n):
        b*= y+1
    return a//b
a,b=map(int,input().split())
print(combi(a,b))