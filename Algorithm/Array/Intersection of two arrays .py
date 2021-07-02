# https://practice.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1#

#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        arr = []
        #code here
        Intersection = []
        i = j = 0
        a.sort()
        b.sort()
        while i < n and j < m:
            if a[i] == b[j]:
 
            # If duplicate already present in Intersection list
                if len(Intersection) > 0 and Intersection[-1] == a[i]:
                    i+= 1
                    j+= 1
 
            # If no duplicate is present in Intersection list
                else:
                    Intersection.append(a[i])
                    i+= 1
                    j+= 1
            elif a[i] < b[j]:
                i+= 1
            else:
                j+= 1
       # print(Intersection)   
        if not len(Intersection):
            return 0
        return len(Intersection)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob = Solution()
        
        print(ob.NumberofElementsInIntersection(a,b,n,m))
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                
# } Driver Code Ends