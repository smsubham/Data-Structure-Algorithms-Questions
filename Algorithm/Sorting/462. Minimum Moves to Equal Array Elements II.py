# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Source: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94937/Java(just-like-meeting-point-problem)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count =0
        i,j = 0,len(nums)-1
        while i<j:
            count += nums[j]-nums[i]
            i+=1
            j-=1
            print(count)
        return count