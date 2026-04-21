class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # UNION FIND!!!!
        # Lets do the DFS solution after!!1


        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        print(adj)


        visited = set()
        def dfs(currNode):
            if currNode in visited:
                return 0
            
            visited.add(currNode)
            print(f"Visited {visited}")
            for edge in adj[currNode]:
                dfs(edge)
            return 1

        connComp = 0
        i = 0
        for i in adj:
            print(f"dfsCall: {i}")
            connComp += dfs(i)

        return connComp


        # par = [i for i in range(n)]
        # rank = [1] * n

        # def find(n1):
        #     res = n1

        #     while res != par[res]:
        #         par[res] = par[par[res]]
        #         res = par[res]
        #     return res

        
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)

        #     if p1 == p2:
        #         return 0
        #     elif rank[p2] > rank[p1]:
        #         par[p1] = p2
        #         rank[p2] += rank[p1]
        #     else:
        #         par[p2] = p1
        #         rank[p1] += rank[p2]
        #     return 1
            
        # res = n
        # for n1, n2 in edges:
        #     res -= union(n1, n2)
        
        # return res