class Solution(object):
    def threeSum(self, nums):
        results = []
        nums.sort()
        
        for i in range(len(nums)-2):
            
            #중복값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #간격 좁혀가며 sum 계산
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    #정답처리
                    results.append([nums[i], nums[left], nums[right]])
                    
                    while left<right and nums[left] == nums[left + 1]:
                        left += 1
                    while left<right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return results
        