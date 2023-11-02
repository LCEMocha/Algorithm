
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        k = 'JFK'
        ticket_dic = collections.defaultdict(list)
        for key, value in sorted(tickets):
            ticket_dic[key].append(value)
        results = []
        
        def dfs(k):
            while ticket_dic[k]:
                next_stop = ticket_dic[k].pop(0)                
                dfs(next_stop)
            results.append(k)
        
        dfs(k)
        return results[::-1]