#https://leetcode.com/problems/global-and-local-inversions/

#https://leetcode.com/problems/global-and-local-inversions/discuss/113656/My-3-lines-C%2B%2B-Solution
#https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution
"""
Explanation
All local inversions are global inversions.
If the number of global inversions is equal to the number of local inversions,
it means that all global inversions in permutations are local inversions.
It also means that we can not find A[i] > A[j] with i+2<=j.
In other words, max(A[i]) < A[i+2]

In this first solution, I traverse A and keep the current biggest number cmax.
Then I check the condition cmax < A[i+2]
"""
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        cmax = 0
        for i in range(len(nums) - 2):
            cmax = max(cmax, nums[i])
            if cmax > nums[i + 2]:
                return False
        return True