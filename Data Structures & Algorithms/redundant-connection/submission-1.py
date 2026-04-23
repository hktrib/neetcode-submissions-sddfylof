class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = len(edges)
        adj = {i : [] for i in range(num_nodes + 1)}


        def has_path(source, target, visited):
            if source == target:
                return True

            visited.add(source)

            for neighbor in adj[source]:
                if neighbor not in visited:
                    if has_path(neighbor, target, visited):
                        return True

            return False

        
        for u, v in edges:
            if has_path(u, v, set()):
                return [u, v]
            
            adj[u].append(v)
            adj[v].append(u)