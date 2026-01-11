#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_list = [""] * numRows
        add = 1 #昇順に文字列を加える時は1、降順の時は-1
        zigzag_idx = 0
        for i in range(len(s)):
            zigzag_list[zigzag_idx] += s[i]
            zigzag_idx += add
            if zigzag_idx == numRows - 1:
                add = -1 #ジグザクの折り返して降順にする
            elif zigzag_idx == 0:
                add = 1 #ジグザクの折り返して昇順にする
        
        return "".join(zigzag_list)
# @lc code=end

