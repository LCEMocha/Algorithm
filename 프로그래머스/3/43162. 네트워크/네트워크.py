def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if not visited[j]:
            visited[j] = True
            for index, connection in enumerate(computers[j]):
                if connection == 1 and not visited[index]:
                    stack.append(index)

def solution(n, computers):
    visited = [False for _ in range(n)]
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            network_count += 1
            
    return network_count