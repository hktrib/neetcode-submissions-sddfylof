class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find by Rank
        num_nodes = len(edges)
        par = [i for i in range(0, num_nodes + 1)]
        rank = [1] * (num_nodes + 1)

        # This function is trying to find the parent of the node
        def find(node):
            parent = par[node]
            # While parent 
            while parent != par[parent]:
                # Path Compression speedup for future
                par[parent] = par[par[parent]]

                parent = par[parent]
            return parent

        # return False if we can't complete
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


         