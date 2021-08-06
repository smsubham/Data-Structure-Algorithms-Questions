# https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

#User function Template for python3

class Solution:
    def longestCommonPrefix(self, strs, n):
        # code here
        
        count =0
        # base case
        if len(strs) ==0:
            return -1
        if len(strs) ==1:
            return strs[0]
        i=0
        while i< len(strs[0]) and i< len(strs[1]) and strs[0][i] == strs[1][i]:
            i += 1
        if i ==0:
            return -1
        prefix = strs[0][:i]
        for str in strs[2:]:
            #if one string is empty then longest common prefix will be empty
            # if i is zero then empty string (-1) is the answer so why continue 
            # further
            if len(str) ==0 or i==0:
                return -1
            i = min(i,len(str))
            if str[:i] != prefix:
                while i>=0 and str[i-1] != prefix[i-1]:
                    i -= 1
            prefix = prefix[:i]
            
        if len(prefix[:i]) ==0:
            return -1
        return prefix[:i]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends