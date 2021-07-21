# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def ordinalOfDate(self, date):
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)