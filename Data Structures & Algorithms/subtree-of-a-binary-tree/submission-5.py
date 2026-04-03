# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot) == True:
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right


    def sameTree(self, curr1: Optional[TreeNode], curr2: Optional[TreeNode]) -> bool:
        if not curr1 and not curr2:
            return True
        elif (not curr1 and curr2) or (curr1 and not curr2):
            return False
        elif curr1.val != curr2.val:
            return False
        
        left = self.sameTree(curr1.left, curr2.left)
        right = self.sameTree(curr1.right, curr2.right)

        return left and right