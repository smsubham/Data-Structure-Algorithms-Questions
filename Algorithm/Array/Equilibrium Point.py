#https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

# Source: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
# O(n) time, O(1) space

# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # finding the sum of whole array
        total_sum = sum(A)
        leftsum = 0
        for i, num in enumerate(A):
             
            # total_sum is now right sum
            # for index i
            total_sum -= num
             
            if leftsum == total_sum:
                return i+1
            leftsum += num
          
          # If no equilibrium index found,
          # then return -1
        return -1

#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends