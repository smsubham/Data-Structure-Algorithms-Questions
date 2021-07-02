# https://practice.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1/?category[]=Strings&category[]=Strings&page=1&query=category[]Stringspage1category[]Strings


#User function Template for python3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        sum = 0
        i=0
        while i< len(s):
        	#print(s[i].isnumeric())
        	temp = []
        	while i<len(s) and s[i].isnumeric():
        		#print(s[i].isnumeric())
        		temp.append(int(s[i]))
        		i+=1
        	i+=1
        	if len(temp)>0:
        		#print(temp)
        		#str = "".join(temp)
        		str1 = ''.join(str(e) for e in temp)
        		#print(str1)
        		sum += int(str1) #print(str1)
        return sum

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