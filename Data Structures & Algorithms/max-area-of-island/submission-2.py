class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            # Check the "not grid[i][j]"
            if  i < 0 or j < 0 or \
                i >= len(grid) or j >= len(grid[0]) or \
                (i, j) in visited or not grid[i][j]:
                return 0
            
            area = 1
            visited.add((i, j))
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            return area


            pass


        max_area_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    max_area_island = max(max_area_island, dfs(i, j))

        return max_area_island