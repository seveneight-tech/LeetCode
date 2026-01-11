#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        str_len = len(s)
        for i in range(str_len):
            if not s_dict.get(s[i]):#該当の文字列がなかった時
                s_dict[s[i]] = t[i]
            elif s_dict[s[i]] != t[i]:
                return False
            if not t_dict.get(t[i]):#該当の文字列がなかった時
                t_dict[t[i]] = s[i]
            elif t_dict[t[i]] != s[i]:
                return False
        return True
                
# @lc code=end