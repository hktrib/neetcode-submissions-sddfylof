# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]

        res = [[root.val]]

        while queue:
            
            level, res_level = [], []

            while queue:
                node = queue.pop(0)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            
            for node in level:
                res_level.append(node.val)

            if res_level:
                res.append(res_level)

            queue = level

        return res


            
                

        