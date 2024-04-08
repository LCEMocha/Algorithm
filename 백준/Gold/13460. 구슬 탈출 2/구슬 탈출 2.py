from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# 구슬과 구멍의 위치 찾기
def locate():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
            elif board[i][j] == 'O':
                ox, oy = i, j
    return rx, ry, bx, by, ox, oy

# 구슬 이동
def move(x, y, dx, dy):
    count = 0  # 이동 거리
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

# BFS 탐색
def bfs(rx, ry, bx, by, ox, oy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        if rx == ox and ry == oy:
            return depth
        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_count = move(bx, by, dx[i], dy[i])
            if nbx == ox and nby == oy:
                continue
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1

rx, ry, bx, by, ox, oy = locate()
print(bfs(rx, ry, bx, by, ox, oy))