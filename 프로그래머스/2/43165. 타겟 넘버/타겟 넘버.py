def solution(numbers, target):
    result = 0
    l = len(numbers)-1
    
    def dfs(index, num):
        nonlocal result
        if index == l:
            if num == target:
                result += 1
            return
        
        # 현재숫자 뺌
        dfs(index+1, num-numbers[index+1])
        
        # 현재숫자 더함
        dfs(index+1, num+numbers[index+1])
    dfs(-1, 0)    
    return result
        