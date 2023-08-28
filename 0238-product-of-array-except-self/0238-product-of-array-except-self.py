class Solution(object):
    def productExceptSelf(self, nums):
        multip = []
        p = 1
        
        #왼쪽 곱셈
        for i in range(len(nums)):
            multip.append(p)
            p = p*nums[i]
            
        #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈    
        p = 1
        for i in range(len(nums)-1, -1, -1):
            multip[i] = multip[i]*p
            p = p*nums[i]
        return multip