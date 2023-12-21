# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                return 'None,'
            return str(node.val) + ',' + dfs(node.left) + dfs(node.right)
        return dfs(root)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def dfs(nodes):
            val = next(nodes)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        
        data_list = iter(data.split(','))
        return dfs(data_list)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))