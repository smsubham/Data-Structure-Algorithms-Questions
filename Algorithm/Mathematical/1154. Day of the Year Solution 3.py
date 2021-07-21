# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        Y,M,D = date.split("-")
        Y = int(Y)
        M = int(M)
        D = int(D)
        if (M > 2 and Y % 4 == 0): 
            D+=1 
        M -=1
        while (M > 0):
            D += days[M - 1]
            M-=1
        return D;