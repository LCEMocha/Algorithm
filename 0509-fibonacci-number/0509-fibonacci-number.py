class Solution:
    def fib(self, n: int) -> int:
        dp = collections.defaultdict(int)
        
        def fib2(i):
            if i <= 1:
                return i
            
            if dp[i]:
                return dp[i]
            dp[i] = fib2(i-1) + fib2(i-2)
            return dp[i]
        
        return fib2(n)
        
        