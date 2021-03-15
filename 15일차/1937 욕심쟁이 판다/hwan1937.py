from sys import stdin
import heapq
from itertools import chain

dy = (-1,0,1,0)
dx = (0,-1,0,1)

n = int(stdin.readline())

board = [list(map(int, stdin.readline().split())) for _ in range(n)]

heap = []
dp = [[1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        heapq.heappush(heap, (board[i][j] * -1, i, j))

while heap:
    num, y, x = heapq.heappop(heap)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > board[y][x]:
            dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)


print(max(chain(*dp)))
