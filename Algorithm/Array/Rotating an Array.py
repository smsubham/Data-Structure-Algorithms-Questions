#https://practice.geeksforgeeks.org/problems/reversal-algorithm5340/1
"""
Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]
"""

#User function Template for python3
class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        d = d%n
        if d ==0:
            return
        self.reverseArray(arr,0,d-1)
        self.reverseArray(arr,d,n-1)
        self.reverseArray(arr,0,n-1)
        
    def reverseArray(self,arr,start,end):
        while start<=end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends