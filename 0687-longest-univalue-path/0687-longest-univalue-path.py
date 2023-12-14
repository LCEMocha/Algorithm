# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            # 왼쪽과 오른쪽 자식 노드에서 시작하는 유니밸류 경로의 길이를 계산합니다.
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            # 왼쪽 및 오른쪽 경로의 길이를 0으로 초기화합니다.
            left_path, right_path = 0, 0

            # 현재 노드의 값이 왼쪽 자식 노드의 값과 같으면, 왼쪽 경로 길이를 업데이트합니다.
            if node.left and node.left.val == node.val:
                left_path = left_len + 1

            # 현재 노드의 값이 오른쪽 자식 노드의 값과 같으면, 오른쪽 경로 길이를 업데이트합니다.
            if node.right and node.right.val == node.val:
                right_path = right_len + 1

            # 최대 유니밸류 경로 길이를 업데이트합니다.
            self.longest = max(self.longest, left_path + right_path)

            # 현재 노드에서 끝나는 최장 유니밸류 경로의 길이를 반환합니다.
            return max(left_path, right_path)

        dfs(root)
        return self.longest
