# https://practice.geeksforgeeks.org/problems/square-root/1

#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        if x ==0: return 0;
        if x ==1: return 1;
        low =0
        high = x//2
        while low <= high:
            mid = (low + high)//2
            if(mid*mid ==x): return mid
            elif mid*mid < x: low = mid +1
            else: high = mid -1
        return low-1
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends