import math
n = int(input())
t = 0
while t < n:
    s = input().split()
    print(int(math.factorial(int(s[1])) / (math.factorial(int(s[1])-int(s[0]))*math.factorial(int(s[0])))))
    t +=1
