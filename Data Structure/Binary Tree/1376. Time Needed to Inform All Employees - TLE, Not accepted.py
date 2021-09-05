#https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        return self.findAdjacentWithTime(headID,manager,informTime)
          
    def findAdjacentWithTime(self,headID,manager,informTime):
        adjacent = []
        for i in range(len(manager)):
            if manager[i] == headID:
                adjacent.append(i)
        #print(adjacent,informTime[headID])
        #No adjacent element then return its waiting time
        if len(adjacent)<1:
            return informTime[headID]
        maxTime = 0
        for adj in adjacent:
            maxTime = max(maxTime,self.findAdjacentWithTime(adj,manager,informTime))
        return maxTime+informTime[headID]