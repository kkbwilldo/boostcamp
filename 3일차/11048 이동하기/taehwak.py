def check(r, c):
    return 0 <= r < n and 0 <= c < m


n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

candies = [[0]*m for _ in range(n)]
candies[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        a = b = c = 0
        if check(i-1,j-1):
            a = candies[i-1][j-1]
        if check(i, j - 1):
            b = candies[i][j - 1]
        if check(i-1,j):
            c = candies[i-1][j]
        candies[i][j] = max(candies[i][j], max(a,b,c) + maze[i][j])

print(candies[n-1][m-1])

