class Solution:
    db = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.db[n]:
            return self.db[n]
        
        self.db[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.db[n]