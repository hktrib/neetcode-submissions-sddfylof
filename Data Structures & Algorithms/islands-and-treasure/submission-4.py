class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = math.pow(2, 31) - 1
        queue = deque()

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.appendleft((row, col))

        print(queue)


        def bfs():

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    

                    # 2 Things to Check
                    # Check if [nr, nc] is in bounds
                    # Check if grid[nr][nc] is a INF (empty room)

                    # Since we are starting from all the Treasure Chests simulatenously
                    #       -> Here simulatenously means that we go 1 step in all directions 
                    #       -> to all available empty rooms
                    # this means that at every point that an empty-room gets filled, the filled distance is 
                    # the closest it can be to a treasure chest
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1

                        queue.append((nr, nc))

            pass
        
        bfs()

        ''' DFS SOLUTION: Takes too much time here.
                -> Why does it take too much time? This is because it starts from every land cell
                -> Each Land Cell does a 4^(M * N) computation in finding the 
        # INF = 2147483647 # math.pow(2, 31) - 1

        # grid can only be traversed up, down, left, or right

        # visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        # def dfs(r, c):
        #     if  r < 0 or c < 0 or \
        #         r >= len(grid) or c >= len(grid[0]) or \
        #         grid[r][c] == -1 or visit[r][c] == True:
        #         return INF
        #     elif grid[r][c] == 0:
        #         return 0

        #     visit[r][c] = True

        #     min_distance = INF
        #     min_distance = min(min_distance, 1 + dfs(r, c + 1))
        #     min_distance = min(min_distance, 1 + dfs(r, c - 1))
        #     min_distance = min(min_distance, 1 + dfs(r + 1, c))
        #     min_distance = min(min_distance, 1 + dfs(r - 1, c))

        #     visit[r][c] = False

        #     return min_distance

        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == INF:
        #             grid[r][c] = dfs(r, c)

         
        # Time Complexity: O(m * n * 4^(m * n))
        # Space Complexity: O(m * n)
        # Problem: This takes way too much time.
        '''
