# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if low <= root.val <= high:
                self.sum += root.val
            if low < root.val:  # 범위 내에 있을 수 있는 왼쪽 서브트리 탐색
                self.rangeSumBST(root.left, low, high)
            if high > root.val:  # 범위 내에 있을 수 있는 오른쪽 서브트리 탐색
                self.rangeSumBST(root.right, low, high)
        return self.sum

        