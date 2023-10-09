import itertools 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
        
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)   
        
        # 예외처리
        if not digits:
            return []
        
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
              '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
              '8':['t','u','v'], '9':['w','x','y','z']}
        result = []
        dfs(0,"")
        
        return result