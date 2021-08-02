# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                #print(i+1,j+1,(j-i)*min(height[i],height[j]))
                area = max(area,  (j-i)*min(height[i],height[j]) )
                
        return area