class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 중복 처리를 위해 먼저 정렬
        results = []
        prev_elements = []

        def dfs(elements):
            if not elements:  # 원소가 없을 때 결과 추가
                results.append(prev_elements[:])
                return

            prev = None  # 중복 처리를 위한 변수
            for i in range(len(elements)):
                if prev == elements[i]:  # 중복된 값은 skip
                    continue

                next_elements = elements[:i] + elements[i+1:]
                prev_elements.append(elements[i])
                dfs(next_elements)
                prev_elements.pop()

                prev = elements[i]  # 현재 원소 저장

        dfs(nums)
        return results
