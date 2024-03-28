from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    # 항공권 정보를 그래프로 변환, 출발지 기준으로 정렬
    for start, end in sorted(tickets, key=lambda x: (x[0], x[1])):
        graph[start].append(end)

    path = []

    def dfs(airport):
        while graph[airport]:
            # 다음 목적지를 pop하여 재귀적으로 탐색
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        path.append(airport)

    # 'ICN'에서 시작하여 DFS 수행
    dfs('ICN')

    # 역순으로 path를 반환 (탐색은 도착지에서부터 거꾸로 진행되므로)
    return path[::-1]