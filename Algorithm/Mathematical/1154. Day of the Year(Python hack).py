# https://leetcode.com/problems/day-of-the-year/
# Credit: https://leetcode.com/problems/day-of-the-year/discuss/355854/Python-Cheat

class Solution:
    def ordinalOfDate(self, date):
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)