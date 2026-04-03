# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minNode, maxNode = None, None
        if q.val == min(p.val, q.val):
            minNode = q
            maxNode = p
        else:
            minNode = p
            maxNode = q

        return self.lowestCommonAncestorHelper(root, minNode, maxNode)

    def lowestCommonAncestorHelper(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root and root.val >= p.val and root.val <= q.val:
            return root
        else:
            if root.val >= p.val:
                return self.lowestCommonAncestorHelper(root.left, p, q)
            else:
                return self.lowestCommonAncestorHelper(root.right, p, q)

