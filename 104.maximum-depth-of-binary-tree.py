#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:return 0 

        candidate_paths = [(root, 1)] #候補となるルートの末端ノードと、その深さを格納する
        depth_max = 0 #深さの最大値
        while candidate_paths != []:
            node, depth = candidate_paths[-1]
            candidate_paths = candidate_paths[:-1] #nodeとdepthを消去
            if node.left == None and node.right == None:
                #nodeが葉だった時
                if depth > depth_max:
                    depth_max = depth
            else:
                #nodeが葉でない時
                if node.left != None:
                    #左のノードを追加
                    candidate_paths.append((node.left, depth + 1))    
                if node.right != None:
                    #右のノードを追加
                    candidate_paths.append((node.right, depth + 1))
                    
        return depth_max
                
                
                
# @lc code=end

