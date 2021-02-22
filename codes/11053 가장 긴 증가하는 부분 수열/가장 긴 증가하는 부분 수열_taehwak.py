from bisect import bisect_left
n = int(input())
A = list(map(int, input().split()))
stack = [A[0]]
for i in range(n):
    if A[i] > stack[-1]:
        stack.append(A[i])
    else:
        stack[bisect_left(stack, A[i])] = A[i]
print(len(stack))