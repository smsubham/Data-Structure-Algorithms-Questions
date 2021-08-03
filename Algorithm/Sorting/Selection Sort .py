# https://practice.geeksforgeeks.org/problems/selection-sort

#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        None
    
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(n):
            #find mimumum
            #minimum = arr[j]
            index = i
            for j in range(i+1,n):
                if arr[index] > arr[j]:
                    #minimum = arr[j]
                    index = j
            #take mimumum to front of i to n part of array.
            arr[i] , arr[index]  = arr[index],arr[i]
        #print(arr)
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends