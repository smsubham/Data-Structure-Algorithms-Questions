# https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1

#User function Template for python3
import math
'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        #code here
        #case 1: when list is empty
        if head ==None: return head1,head2
        temp = head.next
        count = 1
        #count no of elements in the loop
        while temp !=head:
            #prev=temp
            temp = temp.next
            count+=1
        #print(count)
        #part 1 of list
        head1=head
        temp = head
        #print(math.ceil(count/2))
        for i in range(math.ceil(count/2)):
            previous = temp
            temp = temp.next

        #close list1 with None at the end
        head1=head
        previous.next = head1
        
        #part2 of list
        head2=temp
        for i in range(math.ceil(count/2),count):
            previous = temp
            temp = temp.next
        previous.next = head2
        #print(temp.data)
        #prev.next=None
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2

#{ 
#  Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None

def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end = " ")
        tmp = tmp.next
        if tmp == head:
            break
    print()
    
if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1,head2 = obj.splitList(head,head1,head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)


# } Driver Code Ends