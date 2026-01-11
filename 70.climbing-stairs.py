#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        mid = n // 2
        #midに到着するパターン
        stairs_mid = self.climbStairs(mid) * self.climbStairs(n - mid)
        #midに到着しないパターン
        stairs_not_mid = self.climbStairs(mid - 1) * self.climbStairs(n - mid - 1)
        return stairs_mid + stairs_not_mid
    
# @lc code=end

