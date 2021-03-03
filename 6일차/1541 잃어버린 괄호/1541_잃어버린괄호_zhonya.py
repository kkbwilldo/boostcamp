from sys import stdin
stdin=open("bj-study/input.txt","r")
input_math=list(stdin.readline().split("-"))
result=sum(map(int,input_math[0].split("+")))
for x in input_math[1:]:
    if not x.isdecimal():
        result-=sum(map(int,x.split("+")))
    else:
        result-=int(x)
print(result)


        

