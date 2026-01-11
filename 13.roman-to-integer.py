#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] == "I" and s[i + 1] in ["V", "X"]:
                    ans -= 1
                elif s[i] == "X" and s[i + 1] in ["L", "C"]:
                    ans -= 10
                elif s[i] == "C" and s[i + 1] in ["D", "M"]:
                    ans -= 100
                else:
                    ans += Symbol_dict[s[i]]
            else:
                ans += Symbol_dict[s[i]]
            
        return ans
# @lc code=end

