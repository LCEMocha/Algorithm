class Solution:
    def fib(self, n: int) -> int:
        dic = {0:0, 1:1}
        
        def fib2(i):
            if i not in dic:
                dic[i] = fib2(i-1) + fib2(i-2)  
            return dic[i]
        
        return fib2(n)     
        
        