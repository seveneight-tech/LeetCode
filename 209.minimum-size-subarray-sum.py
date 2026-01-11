#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        left = 0
        cur_sum = 0
        min_len = len(nums)
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while cur_sum >= target:
                if right + 1 - left < min_len:
                    min_len = right + 1 - left
                cur_sum -= nums[left]
                left += 1
            
        return min_len

            
        
 
# @lc code=end

