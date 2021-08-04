# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		count = 0
		index = -1 #by default we have to return -1
		for i in range(n):
		    #print(m-count-1)
		    # remember in if we give -ve index then it means we are
		    # starting from end. So this m-count-1 >=0 condition is added.
		    if m-count-1 >=0 and arr[i][m-count-1] ==1:
		        #print(m-count-1)
		        j = m-count-1
		        while j>=0 and arr[i][j] ==1 :
		            count += 1
		            j -= 1
		        index = i
		        #print(count)
		return index
		
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends