from sys import stdin
# stdin=open("bj-study/input.txt","r")
n=stdin.readline()
P = list(map(int,stdin.readline().split()))
P.sort()

def sol(input_p):
    input_p.sort()
    result=0
    for i,p in enumerate(input_p):
        if i>0:
            input_p[i]+=input_p[i-1]
    return sum(input_p)
print(sol(P))