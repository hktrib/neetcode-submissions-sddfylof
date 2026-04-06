"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Two ways
        # Try either recursive BFS or DFS
        # So basically we take a node:
        # send it to function to create and return a copy
        # copy is basically N

        nodes = dict()

        def dfs(node: Optional['Node']):
            if node.val in nodes:
                return nodes[node.val]
            else:
                newNode = Node(node.val)
                nodes[node.val] = newNode

                for neighbor in node.neighbors:
                    newNode.neighbors.append(dfs(neighbor))
                return newNode

        return dfs(node) if node else None
        return 

