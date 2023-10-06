class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        find = []
        right = 1
        if not s:
            return 0
        for i in range(len(s)):
            while right+1 <= len(s) and len(set(s[i:right+1])) == len(s[i:right+1]): 
                right += 1
            find.append(s[i:right])    
            right = i+1
        return len(max(find, key=len))