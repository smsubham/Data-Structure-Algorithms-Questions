#https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        current = head
        prev = None
        while current.next != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        return current