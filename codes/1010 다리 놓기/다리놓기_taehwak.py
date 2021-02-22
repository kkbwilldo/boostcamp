from math import factorial

for _ in range(int(input())):
    left, right = map(int, input().split())
    print(factorial(right)//(factorial(left)*factorial(right-left)))