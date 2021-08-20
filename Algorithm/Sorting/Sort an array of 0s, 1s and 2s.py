# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# O(N) time and space

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
            temp.append(0)
            #print(0)
        for i in range(freq[0],freq[0]+freq[1]):
            temp.append(1)
            #print(1)
        for i in range(freq[1]+freq[0],freq[0]+freq[1]+freq[2]):
            temp.append(2)
            #print(2)
        #print(temp)
        arr[:] = list(temp)


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