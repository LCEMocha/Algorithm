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
        def dfs(node, parent_val):
            if not node:
                return 0

            left_len = dfs(node.left, node.val)
            right_len = dfs(node.right, node.val)

            self.longest = max(self.longest, left_len + right_len)

            # 현재 노드의 값이 부모 노드의 값과 같은 경우,
            # 왼쪽 또는 오른쪽 자식 중 긴 경로를 선택하고 현재 노드를 포함(길이 +1).
            if node.val == parent_val:
                return max(left_len, right_len) + 1

            # 현재 노드의 값이 부모 노드의 값과 다른 경우, 새 경로를 시작해야 하므로 0을 반환합니다.
            return 0

        dfs(root, None)
        return self.longest
