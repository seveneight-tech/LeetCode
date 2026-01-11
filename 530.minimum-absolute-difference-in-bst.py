#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional
import numpy as np
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        values = []
        while queue:
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.popleft()
                values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        #値をソートし、差を計算、最小値を返す
        return np.min(np.sort(np.array(values))[:-1] - np.sort(np.array(values))[1:])
        
# @lc code=end

# queue = deque([root])
# averages = []
# while queue:
#     level_sum, num_nodes = 0, len(queue)
#     for _ in range(num_nodes):
#         node = queue.popleft()
#         level_sum += node.val
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     averages.append(level_sum / num_nodes)
