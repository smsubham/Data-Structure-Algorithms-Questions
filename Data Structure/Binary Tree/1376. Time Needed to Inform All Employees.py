#https://leetcode.com/problems/time-needed-to-inform-all-employees/
#Source: https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532560/JavaC%2B%2BPython-DFS

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)
        def dfs(value):
            """
            We have use "or [0]" to avoid ValueError: max() arg is an empty sequence return max( ) error for leaf nodes with no adjacent elements.
            """
            return max( [dfs(i) for i in children[value]] or [0] )+informTime[value]
        return dfs(headID)