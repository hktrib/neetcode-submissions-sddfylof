class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or \
               i >= len(grid) or j >= len(grid[0]) or \
               (i, j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i, j))
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            
            return


        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print(f"{i} {j}")
                    if (i, j) not in visited:
                        print(f"No. Islands: {num_of_islands} | {i} {j}")
                        num_of_islands += 1
                        dfs(i, j)
                        print(visited)
        
        return num_of_islands