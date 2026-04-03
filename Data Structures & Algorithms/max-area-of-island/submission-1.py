class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(rows) or \
               c not in range(cols) or \
               grid[r][c] == 0:
               return 0
            else:
                grid[r][c] = 0
                return 1 + dfs(r, c + 1) \
                         + dfs(r, c - 1) \
                         + dfs(r + 1, c) \
                         + dfs(r - 1, c) \

        # def bfs(r, c):
        #     area = 1
        #     grid[r][c] = "0"
        #     q = deque()
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc
                    
        #             if nr in range(rows) and \
        #                nc in range(cols) and \
        #                grid[nr][nc] == 1:

        #                 area += 1
        #                 grid[nr][nc] = 0
        #                 q.append((nr, nc))
        #     return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea