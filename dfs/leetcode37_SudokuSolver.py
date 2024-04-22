"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]


"""


from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = 9
        def is_valid(i, j, num):
            for idx in range(n):
                if board[i][idx] == str(num):
                    return False
                if board[idx][j] == str(num):
                    return False
                if board[3*(i//3) + idx//3][3*(j//3)+idx//3] == str(num):
                    return False 
            return True 
        def dfs(i, j):
            """
            Backtracking
            """
            # base case, if the current row is already over the current matrix
            if i == n:
                return True 
            if j == n-1:
                return dfs(i+1, 0)
            
            if board[i][j] == '.':
                for num in range(1,10):
                    if is_valid(i, j, num):
                        board[i][j] = str(num)
                        if dfs(i, j+1): # not only the current valid, but also all the empty spaces will be filled
                            return True 
                        else: # backtracking 
                            board[i][j] = '.'
                # if none are found within the current num
                return False
            # if the current i, j board is not empty, go to the next column 
            else:
                dfs(i, j+1)


def sub_matrix(i,j):
    for idx in range(9):
 # Need to get row 6,7,8 and column 0,1,2
        row = 3 * (i // 3) + idx //  3
        col = 3 * (j //3) + idx // 3
        print(row, col)

sub_matrix(8,2)