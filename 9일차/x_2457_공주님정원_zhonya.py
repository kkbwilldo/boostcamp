from sys import stdin
stdin=open("input.txt","r")
n=int(stdin.readline())
print(n)
month_to_day=[0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
def m2d(input_list):
    day_list=[]
    temp_day1=0
    temp_day2=0
    for i,v in enumerate(input_list):
        if i==0:
            temp_day1+=month_to_day[v]
        elif i==1:
            temp_day1+=v
        elif i==2:
            temp_day2+=month_to_day[v]
        elif i==3:
            temp_day2+=v
    day_list=[temp_day1,temp_day2]
    return day_list
a=[]
for _ in range(n):
    a.append(m2d(map(int,stdin.readline().split())))
b = m2d([3,1,11,30])
print(a)
print(b)
for i in range(n):
    if a[i][0]<=b[0]<=a[i][1]:
        for j in range(i+1,n):
            