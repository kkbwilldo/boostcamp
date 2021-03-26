from sys import stdin
from pprint import pprint

n = int(stdin.readline())
board = []

for _ in range(n):
    board += [list(map(int, stdin.readline().split()))]

if n == 1:
    print(board[0][0])
else:
    for i in range(1,n):
        for j in range(i+1):
            if j == i:
                board[i][j] = board[i-1][j-1] + board[i][j]

            elif j == 0:
                board[i][j] = board[i-1][j] + board[i][j]

            else:
                
                board[i][j] = max(board[i-1][j]+board[i][j], board[i-1][j-1]+board[i][j])

    print(max(board[-1]))
