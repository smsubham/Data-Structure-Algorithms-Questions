# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# O(N) time and O(1) space

#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        freq = [0,0,0]
        temp = []
        #count number of occurrences
        for i in range(len(arr)):
            freq[arr[i]]+=1
        # add those many elements ot the list
        for i in range(freq[0]):
            arr[i] = 0
        for i in range(freq[0],freq[0]+freq[1]):
            arr[i] = 1
        for i in range(freq[1]+freq[0],freq[0]+freq[1]+freq[2]):
            arr[i] = 2



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends