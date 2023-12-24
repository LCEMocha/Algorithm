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
            self.rangeSumBST(root.right, low, high)
            if root.val >= low and root.val <= high:
                print(root.val)
                self.sum += root.val
            self.rangeSumBST(root.left, low, high)
            if root.val >= low and root.val <= high:
                print(root.val)
                self.sum += root.val
        return (self.sum)//2
        