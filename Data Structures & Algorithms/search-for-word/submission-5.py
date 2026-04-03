class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        def dfs(i, j, d, index):
            if index == len(word):
                return True
            else:
                if i + 1 < height:
                    if (i + 1, j) not in d and board[i + 1][j] == word[index]:
                        d[(i + 1, j)] = 1
                        if dfs(i + 1, j, d, index + 1):
                            return True
                        del d[(i + 1, j)]
                if j + 1 < width:
                    if (i, j + 1) not in d and board[i][j + 1] == word[index]:
                        d[(i, j + 1)] = 1
                        if dfs(i, j + 1, d, index + 1):
                            return True
                        del d[(i, j + 1)]
                if i - 1 >= 0:
                    if (i - 1, j) not in d and board[i - 1][j] == word[index]:
                        d[(i - 1, j)] = 1
                        if dfs(i - 1, j, d, index + 1):
                            return True
                        del d[(i - 1, j)]
                if j - 1 >= 0:
                    if (i, j - 1) not in d and board[i][j - 1] == word[index]:
                        d[(i, j - 1)] = 1
                        if dfs(i, j - 1, d, index + 1):
                            return True
                        del d[(i, j - 1)]
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



        