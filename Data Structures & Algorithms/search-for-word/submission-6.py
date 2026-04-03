class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        def dfs(i, j, d, index):
            if index == len(word):
                return True
            else:

                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in directions:
                    ni, nj = dx + i, dy + j
                    if 0 <= ni < height and 0 <= nj < width:
                        if (ni, nj) not in d and board[ni][nj] == word[index]:
                            d[(ni, nj)] = 1
                            if dfs(ni, nj, d, index + 1):
                                return True
                            del d[(ni, nj)]
                return False

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    path = {(i, j): 1}
                    if dfs(i, j, path, 1):
                        return True
        return False
        # do DFS. let's see if i,j will be the start of a matching word in the board
        # def dfs(i, j, dict, index)
        #   if index == len(word):
        #       return True
        #   if i + 1 or j + 1 -1 doesn't go out of bounds
        #      if (i1, j1) not in dict and board[i1][j1] == char:
        #           dfs()
        #      return False 


        

        # Double for loop here that will go through each element and see if board[i][j] matches
        # word[0]
        # put dict {(i, j), 1}
        # helps us avoid going over the same cell

            # if dfs(i, j):
            #   return True



        