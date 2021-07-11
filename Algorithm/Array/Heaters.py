# https://leetcode.com/problems/heaters/

import sys
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        #print(houses)
        #print(heaters)
        
        distance = [sys.maxsize]*len(houses)
        
        #distance from closest RHS
        i=k=0
        while i<len(houses) and k<len(heaters):
            
            if houses[i]<= heaters[k]:
                distance[i] = heaters[k] - houses[i]
                i+=1
            else:
                k+=1
        i=len(houses)-1
        k=len(heaters)-1
        #distance from closest LHS
        while i>=0 and k>=0: 
            if houses[i]>= heaters[k]:
                distance[i] = min(houses[i] - heaters[k] , distance[i] )
                i-=1
            else:
                k-=1
        #print(distance)  
        return max(distance)