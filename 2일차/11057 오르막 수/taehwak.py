from math import factorial

DIV = 10007
def combination_with_replacement(n,r):
    return factorial(n+r-1)//(factorial(n-1)*factorial(r))

n = int(input())
print(combination_with_replacement(10, n)%DIV)
