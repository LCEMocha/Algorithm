class Solution:
    def fib(self, n: int) -> int:
        dp = collections.defaultdict(int)
        
        def fib2(i):
            dp[0] = 0
            dp[1] = 1
            
            for i in range(2, i+1):
                dp[i] = dp[i-1] + dp[i-2]
            
            return dp[i]
        
        return fib2(n)
        
        