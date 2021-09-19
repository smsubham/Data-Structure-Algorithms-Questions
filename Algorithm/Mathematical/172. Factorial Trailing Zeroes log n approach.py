# https://leetcode.com/problems/factorial-trailing-zeroes/
# https://practice.geeksforgeeks.org/problems/trailing-zeroes-in-factorial5134/1

class Solution:
	def trailingZeroes(self, N):
		j = 5
		ans = 0
		while j<=N:
			ans = ans + N//j
			j = j*5

		return ans