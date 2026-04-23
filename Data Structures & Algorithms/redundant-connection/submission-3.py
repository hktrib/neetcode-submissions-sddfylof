class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = len(edges)
        adj = {i : [] for i in range(num_nodes + 1)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        visited = set()         # stores visited nodes during one node's dfs
        removableEdges = set() # stores all edges that create a cycle

        def dfs(curr, prev):
            if curr in visited:
                # not needed possibly
                # if len(visited) == num_nodes:
                # removableEdges.add((prev, curr))
                removableEdges.add((curr, prev))
                return

            visited.add(curr)

            for adjacentNode in adj[curr]:
                if adjacentNode != prev:
                    dfs(adjacentNode, curr)
            return 

        for node in range(1, num_nodes + 1):
            dfs(node, -1)
            visited.clear()

        res = []

        # print(removableEdges)
        
        for i in range(len(edges) - 1, -1, -1):
            n1, n2 = edges[i]

            # possible we need to check both ways
            # n1, n2 and n2, n1

            print(f"{(n1, n2)}")
            if (n1, n2) in removableEdges:
                res = [n1, n2]
                break
        return res