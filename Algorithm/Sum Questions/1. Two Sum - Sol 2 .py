# https://leetcode.com/problems/two-sum/
# Credit: Disscussion Section

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
       #print(type(seen))
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
            #print(seen)
            if remaining in seen: None #3
               #return [seen[remaining],i]  #4
            else:
                seen[value] = i  #5
        print(seen)