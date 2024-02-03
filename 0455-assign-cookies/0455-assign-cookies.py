class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        count = 0
        i,j = 0,0
        while i<=len(g)-1 and j<=len(s)-1:
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count
                