#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        
        return False
# @lc code=end

