# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        #length =1
        #index = 0
        for i in range( len(arr)):
            
            if arr[i]>arr[i+1]:
                return i
                #index = i
        
        #return index