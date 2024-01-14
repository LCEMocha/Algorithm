class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = sorted(nums, key=lambda x: (str(x), -len(str(x))), reverse=True)
        s = [str(i) for i in s]
        s = self.insertion_sort(s)
        return str(int(''.join(s)))
        
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            #key = arr[i]
            j = i - 1
            ss = arr[j:i+1]
            while j >= 0 and int(''.join(ss)) < int(''.join(ss[::-1])):
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                j -= 1
                i -= 1
                ss = arr[j:i+1]
        print(arr)
        return arr
    
    '''
        print(s)
        for i in range(len(s)):
            if i<(len(s)-1) and s[i][0] == s[i+1][0] :
                ss = s[i:i+2]
                if int(''.join(ss)) < int(''.join(ss[::-1])):
                    s[i], s[i+1] = s[i+1], s[i]
    '''
                