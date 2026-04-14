class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        # maintaining all the position that reach PAC and ATL oceans
        pac, atl = set(), set()


        def dfs(r: int, c: int, visit: set, prevHeight: int):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS
                or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])

            pass


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        

        return res