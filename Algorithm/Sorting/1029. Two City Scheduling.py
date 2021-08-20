# https://leetcode.com/problems/two-city-scheduling/
# Source: https://leetcode.com/problems/two-city-scheduling/discuss/297143/Python-faster-than-93-28-ms
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        a = sorted(costs, key=lambda x: x[0]-x[1])
        print(a)
        Sa = 0
        Sb = 0
        for i in range(len(a)//2):
            Sa += a[i][0]
            
        for i in range(len(a)//2, len(a)):
            Sb += a[i][1]
        return Sa + Sb