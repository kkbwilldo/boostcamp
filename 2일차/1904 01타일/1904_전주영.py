n=int(input())
fibo_a,fibo_b=0,1
fibo_now=0
for x in range(1,n+1):
    fibo_now=(fibo_a+fibo_b)%15746
    fibo_a,fibo_b=fibo_b,fibo_now
print(fibo_now)