#https://leetcode.com/problems/pascals-triangle-ii/
#https://www.youtube.com/watch?v=6FLvhQjZqvM&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=9&ab_channel=takeUforward
#https://www.geeksforgeeks.org/find-the-nth-row-in-pascals-triangle/


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # nC0 = 1
        prev = 1
        row  = [1]
        #print(prev, end = '')
        for i in range(1, rowIndex + 1):
            # nCr = (nCr-1 * (n - r + 1))/r
            curr = (prev * (rowIndex - i + 1)) // i
            row.append(curr)
            #print(",", curr, end = '')
            prev = curr
        return row