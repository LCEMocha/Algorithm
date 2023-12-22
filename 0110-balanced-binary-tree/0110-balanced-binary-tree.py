# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            right_height = dfs(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) >= 2:
                return -1  # 높이 차이가 2 이상인 경우 false 반환
            
            return max(left_height, right_height)+1  # 현재 노드의 높이 반환
        return dfs(root) != -1