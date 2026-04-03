class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])


        def dfs(r, c):
            if r not in range(rows) or \
               c not in range(cols) or \
               grid[r][c] == "0":
               return
            else:
               grid[r][c] = "0"

               dfs(r, c + 1)
               dfs(r, c - 1)
               dfs(r + 1, c)
               dfs(r - 1, c)


        # def bfs(r,c):
        #     q = deque()
        #     grid[r][c] = "0"
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc

        #             if nr in range(rows) and \
        #                nc in range(cols) and \
        #                grid[nr][nc] == "1":
        #                q.append((nr, nc))
        #                grid[nr][nc] = "0"



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands