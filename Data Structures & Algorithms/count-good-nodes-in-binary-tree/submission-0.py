# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.goodNodesHelper(root.left, root.val) + self.goodNodesHelper(root.right, root.val)

    def goodNodesHelper(self, root: TreeNode, maxSeen: int) -> int:
        if not root:
            return 0
        else:
            maxSeen = max(maxSeen, root.val)

            if root.val >= maxSeen:
                return 1 + self.goodNodesHelper(root.left, maxSeen) + self.goodNodesHelper(root.right, maxSeen)
            else:
                return self.goodNodesHelper(root.left, maxSeen) + self.goodNodesHelper(root.right, maxSeen)


