# https://practice.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        
        
        arr.sort(); 
    
        count = 0;
        
        for i in range(n - 1, 0, -1):
            l = 0;
            r = i - 1;
            while(l < r):
                if(arr[l] + arr[r] > arr[i]):
                    # If it is possible with a[l], a[r]
                    # and a[i] then it is also possible
                    # with a[l + 1]..a[r-1], a[r] and a[i]
                    count += r - l; 
                    # checking for more possible solutions
                    r -= 1; 
                else:
    
                    # if not possible check for 
                    # higher values of arr[l]
                    l += 1;
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