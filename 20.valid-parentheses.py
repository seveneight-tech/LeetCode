#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        for bracket in list(s):
            #空文字だった場合
            if brackets == []: 
                brackets.append(bracket)
            
            #括弧の種類が一致した場合    
            if brackets[-1] == "(" and bracket == ")":
                brackets.pop()
            elif brackets[-1] == "{" and bracket == "}":
                brackets.pop()
            elif brackets[-1] == "[" and bracket == "]":
                brackets.pop()
            else:
                #括弧の種類が一致しなかった場合  
                brackets.append(bracket)
        return brackets == []
        
# @lc code=end

