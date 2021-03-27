from sys import stdin
from pprint import pprint

N, M = map(int, stdin.readline().split())

board_a = [list(map(str, stdin.readline().rstrip())) for _ in range(N)]
board_b = [list(map(str, stdin.readline().rstrip())) for _ in range(N)]


def change(y, x):

    for i in range(y, y+3):
        for j in range(x, x+3):
            board_a[i][j] = str(1 - int(board_a[i][j]))
    
    
    if board_a == board_b:
        return True
    return False

def chk_board(board_a, board_b):

    global N, M
    answer = 0

    if N < 3 or M < 3:
        if board_a == board_b:
            return 0
        return -1
    
    for i in range(N-2):
        for j in range(M-2):
            if board_a[i][j] == board_b[i][j]:
                continue

            chk = change(i, j)
            answer += 1
            
            if chk:
                return answer
    else:
        return -1

print(chk_board(board_a, board_b))