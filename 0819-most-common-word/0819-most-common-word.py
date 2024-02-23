
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = (re.sub(r"[^\w]", " ", paragraph)).lower().split()
        most_common_char = collections.Counter(paragraph).most_common(len(paragraph))
        for i in range(len(most_common_char)):
            if most_common_char[i][0] not in banned:
                return most_common_char[i][0]
        