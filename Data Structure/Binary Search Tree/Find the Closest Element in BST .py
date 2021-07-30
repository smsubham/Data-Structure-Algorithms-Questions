# https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1

#User function Template for python3

import math

class Solution:
    margin = math.inf
    current = 0
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def minDiff(self,root, target):
        # code here
        # write your code here
        if root == None:
            return
        
        if target == root.data:
            self.current = target
            self.margin =0
            return
        elif target > root.data:
            if abs(target -root.data)<self.margin:
                self.margin = abs(target -root.data)
                self.current = root.data
            self.minDiff(root.right,target)
        else:
            if abs(target -root.data)<self.margin:
                self.margin = abs(target -root.data)
                self.current = root.data
            self.minDiff(root.left,target)
        return int(self.margin)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k=int(input())
        print(Solution().minDiff(root,k))
# } Driver Code Ends