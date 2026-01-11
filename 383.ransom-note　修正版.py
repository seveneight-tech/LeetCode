#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        maga_hash = {}
        for c in magazine:
            maga_hash[c] = 1 + maga_hash.get(c, 0)

        for c in ransomNote:
            if maga_hash.get(c, 0) == 0:
                return False
            else:
                maga_hash[c] -= 1
        return True
# ""aab"\n"baa""
        
# @lc code=end

