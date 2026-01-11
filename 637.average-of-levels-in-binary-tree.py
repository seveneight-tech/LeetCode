#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        cur_node = [root]
        next_node = []
        average_values = []
        node_value = []
        while cur_node != [] or next_node != []:
            if cur_node[-1].left != None: #左に要素がある時
                next_node.append(cur_node[-1].left)
            if cur_node[-1].left != None: #左に要素がある時
                next_node.append(cur_node[-1].right)
            node_value.append(cur_node[-1].val)
            cur_node = cur_node[:-1]
            if cur_node == []:
                #今の階層がすべて調べ終わったら、平均値を格納し一個下の層を調べる
                average_values.append(sum(node_value) / len(node_value))
                cur_node = next_node
                next_node = []
                
        return average_values
                
                
# @lc code=end

