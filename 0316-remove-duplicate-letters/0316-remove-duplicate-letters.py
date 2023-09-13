class Solution(object):
    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                # 스택의 마지막 문자가 현재 문자보다 사전 순서에서 뒤에 있고,
                # 현재 문자 뒤에 해당 문자가 더 있으면 스택에서 제거
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)