# https://leetcode.com/problems/largest-number/
# Credit: https://leetcode.com/problems/largest-number/solution/
# https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
