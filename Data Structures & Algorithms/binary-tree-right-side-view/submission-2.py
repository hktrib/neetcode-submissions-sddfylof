# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res_RSV = []
        res_BFS = []
        q = deque()

        if root:
            q.append(root)

        while q:
            
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res_BFS.append(level)

        for i in range(len(res_BFS)):
            res_RSV.append(res_BFS[i][-1])

        return res_RSV