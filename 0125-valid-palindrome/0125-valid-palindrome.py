class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", s)
        s = ''.join(s.split())
        if s == s[::-1]:
            return True
        return False