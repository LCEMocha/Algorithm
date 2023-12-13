class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        # 그래프 인접리스트 구성
        for s, d, c in flights:
            graph[s].append((d,c))

        dist = collections.defaultdict(lambda: float('inf'))
        dist[(src, k + 1)] = 0

        Q = [(0, src, k + 1)]
        
        while Q:
            cost, node, stops = heapq.heappop(Q)
            if node == dst:
                return cost
            if stops > 0:
                for d, c in graph[node]:
                    next_cost = cost + c
                    if next_cost < dist[(d, stops - 1)]:
                        dist[(d, stops - 1)] = next_cost
                        heapq.heappush(Q, (next_cost, d, stops - 1))

        return -1