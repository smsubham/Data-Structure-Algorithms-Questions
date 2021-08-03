# https://practice.geeksforgeeks.org/problems/insertion-sort/1

#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        currentvalue = alist[index]
        position = index
        
        #We run a loop from j and keep shifting the elements
        #towards right till the element at jth index is greater
        #than element at ith index(key).
        while position>0 and alist[position-1]>currentvalue:
            #Shifting of list elements.
            alist[position]=alist[position-1]
            position = position-1
         
        #Then we just insert the current element(key) at (j+1)th index.    
        alist[position]=currentvalue
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for index in range(1,n):
            #Calling of insert function.
            self.insert(arr, index, n)
        

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends