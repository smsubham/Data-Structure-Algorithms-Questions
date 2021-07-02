# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538

#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        count =0
        i, j = 0, 0
        arr1 =a
        arr2=b
        arr3 = []
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                #print(arr1[i])
                arr3.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                #print(arr2[j])
                arr3.append(arr2[j])
                j+= 1
            else:
                #print(arr2[j])
                arr3.append(arr1[i])
                j += 1
                i += 1
        # Print remaining elements of the larger array
        while i < n:
            #print(arr1[i],"i")
            arr3.append(arr1[i])
            count+=1
            i += 1
        while j < m:
            #print(arr2[j],"j")
            arr3.append(arr2[j])
            count+=1
            j += 1
        #print(count)
        arr3.sort()
        #print(arr3.sort())
        count =1
        for i in range(len(arr3)):
            if i!=0 and arr3[i]!= arr3[i-1]:
                count+=1
        
        return count;
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends