class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A: we are looking to see if the graph is connected
        #       does a graph traversal hit n unique nodes 
        #           len(visited) == n then OK

        # B: We are looking to see if the graph is a valid tree
        #       No Cycles or Loops
        #           get around undirected graph edge case with prev node
        #

        # Let's do a DFS as well to test

        if not n:
            return True

        adj = { i:[] for i in range(n)}

        for vertex, connectedVertex in edges:
            adj[vertex].append(connectedVertex)
            adj[connectedVertex].append(vertex)

        visited = set()

        def dfs(curr : int, prev: int):
            if curr in visited:
                print(f"{prev} | {curr}")
                return False

            visited.add(curr)
            for connectedNode in adj[curr]:
                if connectedNode != prev:
                    if not dfs(connectedNode, curr):
                        return False
            return True

        


        # Problem here is that:
        '''
            If the graph is a tree, the first call will visit every node
            If there's left over nodes its not a tree in the first place

        '''
    
        for i in range(n):
            if i in visited:
                continue
            elif dfs(i, -1) and len(visited) == n:
                print(visited)
                return True
            else:
                return False
            
        return False

        



        



