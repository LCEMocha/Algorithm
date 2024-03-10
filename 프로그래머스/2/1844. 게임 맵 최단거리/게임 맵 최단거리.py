from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [1, -1, 0, 0]  # 이동할 수 있는 방향(상, 하, 좌, 우)
    dy = [0, 0, 1, -1]

    # BFS 함수 정의
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            
            # 현재 위치에서 4가지 방향으로 위치 확인
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 맵 범위를 벗어나는 경우 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                # 벽인 경우 무시
                if maps[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return maps[n-1][m-1]

    answer = bfs(0, 0)
    return answer if answer != 1 else -1