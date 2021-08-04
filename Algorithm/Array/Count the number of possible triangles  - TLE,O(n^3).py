# https://practice.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        arr.sort()
        print(arr)
        count =0
        for i in range(len(arr)):
            for j in  range(i+1,len(arr)):
                for k in  range(j+1,len(arr)):
                    if arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and  arr[k] + arr[j] > arr[i]:
                        count += 1
        return count
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr,n))

# } Driver Code Ends