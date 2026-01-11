#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        for right in range(1, len(s)):
            if s[right] in s[left:right - 1]: #right文字目が重複する
                if right - left > max_len: #重複がない最大文字列
                    max_len = right - left
                left = right #right文字目からまた始める
        
        return max_len
            
                
            
        
        
# @lc code=end

