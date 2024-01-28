class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        most_frequent = 0
        start = 0
        max_len = 0

        for end, char in enumerate(s):
            count[char] += 1
            most_frequent = max(most_frequent, count[char])

            if (end - start + 1) - most_frequent > k:
                count[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len