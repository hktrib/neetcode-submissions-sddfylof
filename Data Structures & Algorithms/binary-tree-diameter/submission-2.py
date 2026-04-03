class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This will store the maximum diameter
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the diameter: it's the max of the current diameter and the path through this node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)

        dfs(root)
        
        # Return the diameter found
        return self.diameter
