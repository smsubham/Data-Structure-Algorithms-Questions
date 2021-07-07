# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1

#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        if n<=1:
            return -1
        left =0
        right = n-1
        # Step 1: Find the potential candidate
        while left <right:
            if M[left][right] ==1:
                left += 1
            else: 
                right -= 1
        # Step 2: Validate the candidate
        candidate = right
        for i in range(n):
            if i != candidate and ( M[candidate][i] or not(M[i][candidate]) ):
                return -1
        return right
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends