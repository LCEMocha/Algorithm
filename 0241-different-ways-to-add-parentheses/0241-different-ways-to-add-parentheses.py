class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def compute(left,right,op):
            answer = []

            for l in left:
                for r in right:
                    answer.append(eval(str(l)+ op +str(r)))
            return answer
    
        if expression.isdigit():
            return [int(expression)]
        
        answer = []
        for i, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                answer.extend(compute(left, right, value))
                
        return answer