#https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1
#https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/

#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        temp = [None]*n
        flag = True
        start,end = 0, n-1
        for i in range(n):
            if flag is True:
                temp[i] = arr[end]
                end -= 1
            else:
                temp[i] = arr[start]
                start += 1
            flag = not(flag)
        #arr.clear()
        arr[:] = list(temp)
        #return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends