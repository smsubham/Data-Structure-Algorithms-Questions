# https://practice.geeksforgeeks.org/problems/red-or-green5711/1/?category[]=Strings&category[]=Strings&page=1&query=category[]Stringspage1category[]Strings#

#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        #code here
        count = [0] * 2
        for c in S:
            if c == 'R':
                count[0]+=1
            else:
                count[1]+=1
        #print(count)
        return min(count)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
# } Driver Code Ends