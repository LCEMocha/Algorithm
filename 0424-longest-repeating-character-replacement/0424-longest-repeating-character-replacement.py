class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.Counter()
        left = right = 0
        for right in range(1, len(s)+1):
            counts[s[right-1]] += 1
            
            # 가장 흔한 문자
            max_char_n = counts.most_common(1)[0][1]
            
            # k초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right-left
        