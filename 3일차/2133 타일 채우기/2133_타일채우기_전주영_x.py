# n=int(input())
def sol(n):
    result=0
    if n%2==1:
        result=0
    else:
        result=3**(n//2)
    print(result)
for x in range(1,30):
    sol(x)