from collections import deque

n, m = map(int, input().split())  # 세로 크기 N과 가로 크기 M을 입력받음
board = [list(input().strip()) for _ in range(n)]  # 미로 정보 입력받음
red, blue = None, None

# 구슬과 구멍의 초기 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)

# 상, 하, 좌, 우 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    count = 0  # 이동한 칸 수
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    visited = {}
    global red
    global blue
    queue = deque([(red, blue, 1)])
    visited[red, blue] = True

    while queue:
        red, blue, count = queue.popleft()
        if count > 10:  # 10회 이상 움직였다면 실패
            break
        for i in range(4):
            nrx, nry, r_count = move(red[0], red[1], dx[i], dy[i])
            nbx, nby, b_count = move(blue[0], blue[1], dx[i], dy[i])

            if board[nbx][nby] != 'O':  # 파란 구슬이 구멍에 빠지지 않은 경우
                if board[nrx][nry] == 'O':  # 빨간 구슬이 구멍에 빠진 경우
                    return count
                if nrx == nbx and nry == nby:  # 구슬이 겹치는 경우
                    if r_count > b_count:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    visited[(nrx, nry, nbx, nby)] = True
                    queue.append(((nrx, nry), (nbx, nby), count + 1))
    return -1


print(bfs())
