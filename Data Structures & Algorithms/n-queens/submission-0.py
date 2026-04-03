from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []

        def calcNQueens(row_index, curr_board):
            # Base case: placed all queens
            if row_index == n:
                sols.append(curr_board)
                return
            
            for c in range(n):
                valid = True
                for (r, col) in curr_board:
                    if self.is_same_row(row_index, r) or \
                       self.is_same_col(c, col) or \
                       self.is_same_diagonal(row_index, r, c, col):
                        valid = False
                        break
                if valid:
                    calcNQueens(row_index + 1, curr_board + [(row_index, c)])

        calcNQueens(0, [])

        # Convert list of tuples to list of strings ('.' and 'Q')
        def board_to_str(board):
            result = []
            for r, c in board:
                row_str = ['.'] * n
                row_str[c] = 'Q'
                result.append("".join(row_str))
            return result

        return [board_to_str(sol) for sol in sols]

    def is_same_row(self, r1, r2):
        return r1 == r2

    def is_same_col(self, c1, c2):
        return c1 == c2

    def is_same_diagonal(self, r1, r2, c1, c2):
        return abs(r1 - r2) == abs(c1 - c2)
