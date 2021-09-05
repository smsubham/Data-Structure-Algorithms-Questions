#https://leetcode.com/problems/merge-two-sorted-lists/

#Source: https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if a and b:
            if a.val > b.val:
                a, b = b, a
            print(a.val,b.val)
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

