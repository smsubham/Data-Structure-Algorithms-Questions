#https://leetcode.com/problems/pascals-triangle/
#Doesn't work in python 3
#https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res += list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))
        return res[:numRows]

