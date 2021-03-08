from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().split())
red, blue, hole = None, None, None
board = [list(map(str,stdin.readline().rstrip('\n'))) for _ in range(N)]

# 빨간 구슬 2차원 + 파란 구슬 2차원
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# BFS 하는데 사용하는 큐
q = deque()

for n in range(N):
    
    if 'R' in board[n]:
        red = [n, board[n].index('R')]
    if 'B' in board[n]:
        blue = [n, board[n].index('B')]
    

# 상하좌우 이동
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 빨간 구슬과 파란 구슨 위치 True
visited[red[0]][red[1]][blue[0]][blue[0]] = True
# 시작 값 queue append
q.append((red[0], red[1], blue[0], blue[1], 1))


def move(y, x, dy, dx):
    count = 0   # 몇칸 이동했는지

    # 벽의 끝까지 가거나 구멍까지 이동    
    while board[y+dy][x+dx] != "#" and board[y][x] != 'O':
        y += dy
        x += dx
        count += 1
    
    return y, x, count


def bfs():
    # 큐가 있을때 동안 반복
    while q:
        
        ry, rx, by, bx, depth = q.popleft()
        
        # 만약 10번 이상인 경우 스탑
        if depth > 10:
            break
        for i in range(4):
            # 벽 or 구멍까지 이동.
            next_ry, next_rx, r_count = move(ry, rx, dy[i], dx[i])
            next_by, next_bx, b_count = move(by, bx, dy[i], dx[i])

            # 파란색 구슬이 빠지는 경우
            if board[next_by][next_bx] == 'O':
                continue
            
            # 빨간색 구슬이 빠지는 경우
            if board[next_ry][next_rx] == 'O':
                print(depth)
                return
            
            # 빨간색 구슬과 파란색 구슬이 같이 위치인 경우
            if next_ry == next_by and next_rx == next_bx:
                # 빨간색 구슬이 더 많이 움직인 경우
                if r_count > b_count:
                    next_ry -= dy[i]
                    next_rx -= dx[i]
                # 파란색 구슬이 더 많이 움직인 경우
                else:
                    next_by -= dy[i]
                    next_bx -= dx[i]
            
            # 해당 위치에 방문하지 않았으면 방문체크 이후 큐에 추가.
            if not visited[next_ry][next_rx][next_by][next_bx]:
                visited[next_ry][next_rx][next_by][next_bx] = True
                q.append((next_ry, next_rx, next_by, next_bx, depth+1))
    print(-1)

bfs()
