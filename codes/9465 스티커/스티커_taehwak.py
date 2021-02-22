def solution():
    n = int(input())
    stickers = [[0] + list(map(int, input().split())) for _ in range(2)]
    for i in range(2, n + 1):
        stickers[0][i] += max(stickers[1][i - 1], stickers[1][i - 2])
        stickers[1][i] += max(stickers[0][i - 1], stickers[0][i - 2])
    return max(stickers[0][n], stickers[1][n])


for i in range(int(input())):
    print(solution())
