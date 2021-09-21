#https://leetcode.com/problems/sort-array-by-parity/
#O(n) time, note while and for combined work is for n steps only. O(1) space.


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        boundary = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]%2 ==1:
                #check next element
                boundary += 1
                #while ends when we find next even number or reach end of list.
                while boundary < n and nums[boundary] %2 ==1:
                    boundary += 1
            if boundary>=n:
                break
            #print(nums)
            nums[boundary], nums[i] = nums[i],nums[boundary]
            #print(i,boundary,nums)
            #to prevent i going beyond current boundary
            boundary = max(i,boundary)
        return nums