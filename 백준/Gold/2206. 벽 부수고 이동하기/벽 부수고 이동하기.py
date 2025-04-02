from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

def bfs():
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 1, 0))  # x, y, length, broken
    visited[0][0][0] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y, l, broken = queue.popleft()

        if x == n-1 and y == m-1:
            return l

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx, ny, l+1, broken))
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, l+1, 1))

    return -1

print(bfs())
