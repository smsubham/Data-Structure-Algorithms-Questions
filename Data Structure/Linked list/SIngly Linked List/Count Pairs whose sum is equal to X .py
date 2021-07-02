# https://practice.geeksforgeeks.org/problems/count-pairs-whose-sum-is-equal-to-x/1

#Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
        


 # } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        '''
        h1:  head of linkedList 1
        h2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:   len of linkedList 1
        X:   given sum
        '''
        high = max(n1,n2)
        list1 = set()
        list2 = set()
        while h1!=None:
            list1.add(h1.data)
            h1 = h1.next
        while h2!=None:
            list2.add(h2.data)
            h2 = h2.next   
        #print(list1)
        #print(list2)
        sum_list = []
        for nums in list1:
            if x-nums in list2: sum_list.append((nums,x-nums))
        #print(sum_list)
        return len(sum_list)
        
        

#{ 
#Driver Code Starts.
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        X=int(input())
        
        
        print(Solution().countPair(ll1.head,ll2.head,n1,n2,X))


#} Driver Code Ends