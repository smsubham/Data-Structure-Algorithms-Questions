# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head == None:
            return head
        
        point = head
        n=1
        #count nuber of nodes
        while point.next != None:
            #print(point.val)
            n+=1
            point = point.next
        #print(point.val, n)
        #if k is multiple of n then after rotations also list is same, so just
        #return current list.
        if k % n ==0:
            return head
        # k%n done so that net effect of rotation can be used, like for n rotation the
        # list becomes what it was before
        # n- (k % n), so so we travel to the end of list part which isn't rotated
        travel = n- (k % n)
        temp = head
        while travel >1:
            travel -=1
            temp = temp.next
        #print(temp.val, travel)
        new = temp.next #new head location
        # temp point to end of list part which isn't rotated, so now it will be None as it
        # will be new list end.
        temp.next = None
        #traverse part of list which needs to be moved to front/
        point = new
        while point.next != None:
            #print(point.val)
            point = point.next
        #end of rotated list will point to original head
        point.next = head
        #new head will start from next node of part which wasn't to be rotated.
        head = new
        
        return head