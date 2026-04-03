# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional [TreeNode]) -> int:
        mpSum = [float('-inf')]
        def maxPathSumHelper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            else:
                leftSum = max(0, maxPathSumHelper(node.left))
                rightSum = max(0, maxPathSumHelper(node.right))

                mpSum[0] = max(node.val + leftSum + rightSum, mpSum[0]) 
                return node.val + max(leftSum, rightSum)

        maxPathSumHelper(root)
        return mpSum[0]