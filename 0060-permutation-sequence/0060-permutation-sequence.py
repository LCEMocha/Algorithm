class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 팩토리얼 값을 계산하는 도우미 함수
        def factorial(num):
            if num == 0:
                return 1
            return num * factorial(num - 1)
        
        numbers = list(range(1, n+1))
        k -= 1  # 인덱스는 0부터 시작하므로 1을 빼준다.
        res = []
        
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            res.append(numbers.pop(index))
        
        return ''.join(map(str, res))