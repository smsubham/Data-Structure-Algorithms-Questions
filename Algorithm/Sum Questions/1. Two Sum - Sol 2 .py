# https://leetcode.com/problems/two-sum/
# Credit: Disscussion Section
#https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #print(type(seen))
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
            #print(seen)
            if remaining in seen:  #3
			#if a number shows up in the dictionary already that means the necesarry pair has been iterated on previously
                return [seen[remaining],i]  #4
            else: # else is entirely optional
                seen[value] = i  #5
			# we insert the required number to pair with should it exist later in the list of numbers