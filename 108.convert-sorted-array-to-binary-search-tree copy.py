#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #回答を見て解いた

        #根となるノードを追加
        if not nums:
            return None
        nums_mid = int(len(nums) / 2)
        head = TreeNode(val=nums[nums_mid])
        
        #左側に付くノードを追加
        head.left = self.sortedArrayToBST(nums[:nums_mid])
        #右側に付くノードを追加
        head.right = self.sortedArrayToBST(nums[nums_mid + 1:])
        
        return head
        
        
# @lc code=end

