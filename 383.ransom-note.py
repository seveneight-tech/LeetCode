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
        list_ransomNote = list(ransomNote)
        list_magazine = list(magazine)
        correct_num = 0
        for i in range(len(list_ransomNote)):
            if list_ransomNote[i] in list_magazine:
                list_magazine.remove(list_ransomNote[i])
                correct_num += 1
            else:
                break
        return len(list_ransomNote) == correct_num
    
# ""aab"\n"baa""
        
# @lc code=end

