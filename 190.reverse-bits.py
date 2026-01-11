#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n_list = []
        binary_length = 32
        for i in range(binary_length):
            n_list.append(n % 2)
            n = n // 2
        
        return sum([x * 2 ** i for i, x in enumerate(n_list[::-1])])
    
# @lc code=end

