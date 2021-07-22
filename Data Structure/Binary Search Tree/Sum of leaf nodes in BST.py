# https://practice.geeksforgeeks.org/problems/sum-of-leaf-nodes-in-bst/1

#User function Template for python3

##Structure of node
'''
class Node:
    data=0
    left=None
    right=None

'''
def sumOfLeafNodes(root):
    #Your code here
    
    #sumUtil()
    
    if root == None:
        return 0
    
    if root.left == None and root.right == None:
        return root.data
    
    return sumOfLeafNodes(root.left) + sumOfLeafNodes(root.right)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    data=0
    left=None
    right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root


    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
        print(sumOfLeafNodes(root))
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends