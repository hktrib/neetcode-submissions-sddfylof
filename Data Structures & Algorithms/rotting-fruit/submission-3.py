class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Observations:
            -> Fresh fruit only island not adjacent (either horizontally/vertically)
               to any other fruit will not rot despite how many minutes pass

            -> If there is a rotten fruit in the island
                -> all adjacent fruits will rot every minutes (1 -> 2)
            

            -> One tactic is to locate all the rotten fruits and then start to multi-BFS
                from there. 


            Multi-BFS:
                -> Get the count of all fresh fruits
                -> Locate all the rotten fruits and dump into a queue
  


        '''

        fresh_fruits = 0
        queue = deque()

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        minutes = 0


        def bfs():

            nonlocal fresh_fruits, minutes
            while queue:
                # popleft() pops from the front of the queue a rotten fruit
                rot = False
                minute, r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if  0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rot = True
                        fresh_fruits -= 1
                        queue.append((minute + 1, nr, nc))
                
                if not queue:
                    minutes = minute

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    # appendleft() places elements at beginning
                    # doing it to troll and get comfortable with this
                    queue.appendleft((0, r,c))
        bfs()

        print(f"minutes = {minutes} | fresh_fruits = {fresh_fruits}")
        
        return -1 if fresh_fruits > 0 else minutes
        