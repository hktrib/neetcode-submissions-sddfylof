
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        q, res = [root], []
        
        while q:
            node = None
            for i in range(len(q)):
                node = q.pop(0)
                
                if node.left:   
                    q.append(node.left)
                
                if node.right:  
                    q.append(node.right)
            
            res.append(node.val)
        
        return res