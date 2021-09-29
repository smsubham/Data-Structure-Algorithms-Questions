#https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
"""
Intuition
We all know the distributive property that (a1+a2)*(b1+b2) = a1*b1 + a1*b2 + a2*b1 + a2*b2

Now focus on each bit,
for example the last bit of A[i] and B[j], and think how it works and affect the result.

Explanation
Distributive property is similar for AND and XOR here.
(a1^a2) & (b1^b2) = (a1&b1) ^ (a1&b2) ^ (a2&b1) ^ (a2&b2)
(I wasn't aware of this at first either)

Complexity
Time O(A + B)
Space O(1)
"""

#https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/discuss/1163992/JavaC%2B%2BPython-Easy-and-Concise-O(1)-Space
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)