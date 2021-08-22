# https://leetcode.com/problems/missing-number/
#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
#https://www.geeksforgeeks.org/find-the-missing-number/
""" 
Modification for Overflow  
Approach: The approach remains the same but there can be overflow if n is large. In order to avoid integer overflow, pick one number from known numbers and subtract one number from given numbers. This way there won’t have Integer Overflow ever.
Algorithm: 
Create a variable sum = 1 which will store the missing number and a counter variable c = 2.
Traverse the array from start to end.
Update the value of sum as sum = sum – array[i] + c and update c as c++.
Print the missing number as a sum.
"""
# a represents the array
# n : Number of elements in array a
def getMissingNo(a, n):
	i, total = 0, 1

	for i in range(2, n + 2):
		total += i
		total -= a[i - 2]
	return total
#XOR Method, quite slow beats only 60% solutionn
#Source: https://leetcode.com/problems/missing-number/discuss/69786/3-different-ideas%3A-XOR-SUM-Binary-Search.-Java-code
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res
