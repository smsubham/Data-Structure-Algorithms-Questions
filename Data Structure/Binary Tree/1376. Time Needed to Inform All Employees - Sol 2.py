#https://leetcode.com/problems/time-needed-to-inform-all-employees/
#Source: https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532560/JavaC%2B%2BPython-DFS

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            #check if its already covered with dfs or its root node.
            print("A",i)
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                #so that we do dfs on node only once
                manager[i] = -1
                print("B",i)
            return informTime[i]
        return max(map(dfs, range(n)))