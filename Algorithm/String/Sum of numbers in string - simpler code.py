# https://practice.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1/?category[]=Strings&category[]=Strings&page=1&query=category[]Stringspage1category[]Strings

#Back-end complete function Template for Python 3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        temp = "0"
        Sum = 0
      
        #iterating over the string.
        for ch in s:
      
            #if current character is digit, we store it in a temporary string.
            if (ch.isdigit()):
                temp += ch
      
            else:
                #incrementing final sum by number stored in temporary string.
                Sum += int(temp)
                #making the temporary string empty again.
                temp = "0"
      
        #adding any number if it's present in temporary
    	#string to final sum and returning it.
        return Sum + int(temp)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        s=str(input())
        obj = Solution()
        print(obj.findSum(s))
# } Driver Code Ends