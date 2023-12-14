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
            if node.val == parent_val:
                return max(left_len, right_len) + 1
            return 0

        dfs(root, None)
        return self.longest
