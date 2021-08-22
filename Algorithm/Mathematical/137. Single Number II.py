#https://leetcode.com/problems/single-number-ii/
#Source: https://leetcode.com/problems/single-number-ii/discuss/43294/Challenge-me-thx
# See above for intuition
# Detailed Explanation: https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
# Generic idea for these kind of question: https://leetcode.com/problems/single-number-ii/discuss/43296/An-General-Way-to-Handle-All-this-sort-of-questions.
"""
So, effectively, any number that appears a first time will be in set "ones" so it will not be added to "twos". Any number appearing a second time would have been removed from set "ones" in the previous step and will now be added to set "twos". Lastly, any number appearing a third time will simply be removed from the set "twos" and will no longer exist in either set.
Finally, once we are done iterating over the entire list, set "twos" would be empty and set "ones" will contain the only number that appears once.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones
        return ones