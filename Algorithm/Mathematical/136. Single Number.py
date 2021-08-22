# https://leetcode.com/problems/single-number/
# Source: https://leetcode.com/problems/single-number/discuss/42997/My-O(n)-solution-using-XOR
# known that A XOR A = 0 and the XOR operator is commutative, the solution will be very straightforward. Also A xor 0 = A, so at the end only number not repeated is left.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missing = 0
        for num in nums:
            missing ^= num
        return missing