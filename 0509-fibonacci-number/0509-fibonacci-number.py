class Solution:
    def fib(self, n: int) -> int:
        dic = {0:0, 1:1}
        
        def fib2(i):
            if i in dic:
                return dic[i]
            return fib2(i-1) + fib2(i-2)
        
        if n not in dic:
            dic[n] = fib2(n)
        
        
        return fib2(n)
        
        