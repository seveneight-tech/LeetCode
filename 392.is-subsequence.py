#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        t_index = 0
        while list_s:
            if list_s[0] in list_t[t_index:]:
                t_index = list_t[t_index:].index(list_s[0])
                del list_s[0]
            else:
                return False
        return True
# @lc code=end

