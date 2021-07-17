# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        point = head
        count =1
        while point.next != None:
            count+=1
            point = point.next
        #store head of each part in this list, its None by default
        headPointer = [None] * k
        
        point = head
        moveTill = ceil(count/k) # how many items to include in each list
        j =0  #stores the list number we are currently in
        while point != None:
            #store head of each part in this list, j points to which list we are in.
            headPointer[j] = point
            print(point.val)
            tempCount =0
            for i in range(moveTill):
                point = point.next
            j+=1
            
        return headPointer