#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        FinalRoman = []
        
        Roman_one = ["I", "X", "C", "M"] #1のけた
        Roman_five = ["V", "L", "D"] #5のけた
        
        #千、百、十の順に代入していく
        for i in range(3, -1, -1):
            digit = num // (10 ** i)
            if digit == 4:
                FinalRoman.append([Roman_one[i], Roman_five[i]])
            elif digit == 9:
                FinalRoman.append([Roman_one[i], Roman_one[i + 1]])
            elif digit > 5:
                FinalRoman.append([Roman_five[i]])
                FinalRoman.append([Roman_one[i]] ** (digit % 5))
            else:
                FinalRoman.append([Roman_one[i]] ** digit)
        
        return FinalRoman
        
# @lc code=end

