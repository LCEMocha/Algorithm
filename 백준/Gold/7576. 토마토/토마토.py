import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int, input().split())

graph = []
queue = deque([])
visited = [[False] * m for _ in range(n)]
number_of_pm1 = 0

for ni in range(n):
    tomato = list(map(int, input().split()))
    for mi in range(m):
        if tomato[mi] == 1:
            queue.append((ni, mi, 0))
            number_of_pm1 += 1
            visited[ni][mi] = True
        elif tomato[mi] == -1:
            number_of_pm1 += 1
    graph.append(tomato)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
all_tomato_ripe = n*m - number_of_pm1

def bfs(n, m, all_tomato_ripe):
    global visited
    global graph
    global queue

    if all_tomato_ripe == 0:
        return 0

    while queue:
        y, x, count = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] == 0:
                queue.append((ny, nx, count+1))
                visited[ny][nx] = True
                graph[ny][nx] = 1
                all_tomato_ripe -= 1
                if all_tomato_ripe == 0:
                    return count+1
    return -1

print(bfs(n, m, all_tomato_ripe))