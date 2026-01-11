#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # #リストがいずれも空の場合
        # if list1 is None and list2 is None:return None
        # #リストがいずれか空の場合
        # if list1 is None: return list2
        # if list2 is None: return list1

        # #返すリストの初期化　値が小さい方から始める
        # if list1.val <= list2.val:
        #     #リスト1の先頭の要素のほうが値が小さいならリスト1の先頭の要素を追加する
        #     merge_list = ListNode(list1.val)
        #     list1 = list1.next
        # else:
        #     merge_list = ListNode(list2.val)
        #     list2 = list2.next
        merge_list = ListNode()
        answer_list = merge_list
        while list1 and list2:
            if list1.val <= list2.val:
                #List1が最後まで移動しておらず、List2が最後まで移動した、またはlist1の値が小さい時
                # merge_listにlist1のノードを追加
                merge_list.next = list1 #修正、nextに全て入れてしまい、後で修正する
                merge_list = merge_list.next
                list1 = list1.next
            else:
                #List2の値の方が大きい時
                # merge_listにlist2のノードを追加
                merge_list.next = list1 #修正、nextに全て入れてしまい、後で修正する
                merge_list = merge_list.next
                list2 = list2.next
            
        
        #どちらかが空になったら、最後に他方のリストを全て追加する。
        if list1:
            merge_list.next = list1
        else:
            merge_list.next = list2
        return answer_list.next #nextすることにより、最初の要素を無視できる。
                
# @lc code=end

