from sys import stdin
from itertools import chain

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    temp = list(map(str, input()))
    matrix.append([int(i) for i in temp])


for i in range(1, n):
    for j in range(1, m):
        
        if matrix[i][j] == 1:
            matrix[i][j] += min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])

# for a in range(n):
#     print(matrix[a])

res = list(chain(*matrix))
print(max(res) ** 2)