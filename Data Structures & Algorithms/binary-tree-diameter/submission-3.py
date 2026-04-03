# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)

                self.diameter = max(self.diameter, left + right)

                return 1 + max(left, right)

        if root == None:
            return 0
        
        dfs(root)

        return self.diameter
        pass
        