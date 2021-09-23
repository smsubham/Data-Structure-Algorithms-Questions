#https://practice.geeksforgeeks.org/problems/number-of-pairs-1587115620/1


#User function Template for python3

class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,a,b,M,N):
        #code here
        ans = 0
        for i in range(M):
            for j in range(N):
                if (pow(a[i], b[j]) > pow(b[j], a[i])):
                    ans += 1
        return ans

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