from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if nx<0 or ny<0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    queue.append((nx, ny))
                    
        return maps[n-1][m-1]
    
    answer = bfs(0,0)
    return answer if answer != 1 else -1
            