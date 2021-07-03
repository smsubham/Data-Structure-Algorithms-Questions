# https://practice.geeksforgeeks.org/problems/rotate-by-90-degree0356/1

#User function Template for python3

def rotate(mat):
    
    # Consider all squares one by one
    for x in range(0, int(N / 2)):
        
        # Consider elements in group   
        # of 4 in current square
        for y in range(x, N-x-1):
            
            # store current cell in temp variable
            mat[x][y],mat[y][N-1-x],mat[N-1-x][N-1-y],mat[N-1-y][x] = mat[y][N-1-x], mat[N-1-x][N-1-y],mat[N-1-y][x],mat[x][y] 
            """
            # move values from right to top
            mat[x][y] = mat[y][N-1-x]

            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]

            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]

            # assign temp to left
            mat[N-1-y][x] = temp
            """
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends