import itertools 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
              '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
              '8':['t','u','v'], '9':['w','x','y','z']}
        
        # digits의 각 숫자에 해당하는 문자 리스트를 lookup
        lookup = [dic[digit] for digit in digits]
        
        # product를 사용해 모든 조합 구하기
        combinations = [''.join(combination) for combination in itertools.product(*lookup)]
        
        return combinations
        