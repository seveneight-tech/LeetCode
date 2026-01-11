#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
import numpy as np

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.board(board)
        for i in range(9): #行ごとにチェック
            num_list = [int(num) for num in board[i] if num != "."]
            if list(set(num_list)) != num_list:
                return False
        
        for i in range(9): #列ごとにチェック
            num_list = [int(num) for num in board[:, i] if num != "."]
            if list(set(num_list)) != num_list:
                return False
        
        print(board[0:3, 0:3])

        for i in range(3):
            for j in range(3): #3*3マスごとにチェック
                num_list = [int(num) for num in board[3*i:3*(i+1), 3*j:3*(j+1)] if num != "."]
                if list(set(num_list)) != num_list:
                    return False
        
        return True
# @lc code=end

