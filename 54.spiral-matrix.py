#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer_list = []
        up = 0
        down = len(matrix)
        right = len(matrix[0])
        left = 0
        while up < down and left < right:
            #上部
            for i in range(left, right):
                answer_list.append(matrix[up][i])
            up += 1
            
            #右部
            for i in range(up, down):
                answer_list.append(matrix[i][right])
            right -= 1
            
            #下部
            for i in range(right, left, -1):
                answer_list.append(matrix[down][i])
            down -= 1
            
            #左部
            for i in range(down, up, -1):
                answer_list.append(matrix[i][left])
            left += 1
        
        return answer_list
                
            
        
        
# @lc code=end

