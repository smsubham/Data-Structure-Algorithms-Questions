# https://practice.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list

#User function Template for python3

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteNode(self,head, x):
        # Code here
        if head == None: return 
        if x==0: return 
        #case 1: If head is to be deleted
        #print(head.next)
        if x==1 and head.next != None:
            #print(head.data)
            head = head.next
            head.prev = None
            #print(head.data)
            return
        #>1 node and delete head node
        if x==1:
            #print(head.data)
            head = head.next
            #head.prev = None
            #print(head.data)
            return None
        
        
        
        temp = head
        previous = head
        count =1
        while temp.next !=None:
            if x==count:
                break
            count+=1
            previous = temp
            temp = temp.next
        #case 2: If last node is to be deleted we just need t set previous node
        # to None.
        if temp.next == None:
            previous.next = None
        #case 3: If any intermediate node is to be deleted
        else:
            previous.next = temp.next
            temp.next.prev = previous
        return head
#{ 
#  Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        pos = int(input())
        Solution().deleteNode(llist.head, pos)
        llist.printList(llist.head)
# Contributed by: Harshit Sidhwa

                               
# } Driver Code Ends