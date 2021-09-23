#https://practice.geeksforgeeks.org/problems/number-of-pairs-1587115620/1
#https://www.geeksforgeeks.org/find-number-pairs-xy-yx/


import bisect
#User function Template for python3

class Solution:
    
    
    # Function to return count of pairs
    # with x as one element of the pair.
    # It mainly looks for all values in Y
    # where x ^ Y[i] > Y[i] ^ x
     
     
    def count(self,x, Y, n, NoOfY):
     
        # If x is 0, then there cannot be
        # any value in Y such that
        # x^Y[i] > Y[i]^x
        if x == 0:
            return 0
     
        # If x is 1, then the number of pairs
        # is equal to number of zeroes in Y
        if x == 1:
            return NoOfY[0]
     
        # Find number of elements in Y[] with
        # values greater than x, bisect.bisect_right
        # gets address of first greater element
        # in Y[0..n-1]
        idx = bisect.bisect_right(Y, x)
        ans = n - idx
     
        # If we have reached here, then x must be greater than 1,
        # increase number of pairs for y=0 and y=1
        ans += NoOfY[0] + NoOfY[1]
     
        # Decrease number of pairs
        # for x=2 and (y=4 or y=3)
        if x == 2:
            ans -= NoOfY[3] + NoOfY[4]
     
        # Increase number of pairs
        # for x=3 and y=2
        if x == 3:
            ans += NoOfY[2]
     
        return ans
         
    #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,X,Y,m,n):
        #code here
        # To store counts of 0, 1, 2, 3,
        # and 4 in array Y
        NoOfY = [0] * 5
        for i in range(n):
            if Y[i] < 5:
                NoOfY[Y[i]] += 1
     
        # Sort Y so that we can do binary search in it
        Y.sort()
        total_pairs = 0  # Initialize result
     
        # Take every element of X and
        # count pairs with it
        for x in X:
            total_pairs += self.count(x, Y, n, NoOfY)
     
        return total_pairs

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        M,N=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        ob=Solution();
        print(ob.countPairs(a,b,M,N))
        #code here
# } Driver Code Ends