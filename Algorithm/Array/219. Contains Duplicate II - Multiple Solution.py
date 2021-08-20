# https://leetcode.com/problems/contains-duplicate-ii/
# Source: https://leetcode.com/problems/contains-duplicate-ii/discuss/918012/Simple-python-solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        myDict={}
        
        for i in range(len(nums)):
            
            if nums[i] in myDict and abs(i-myDict[nums[i]])<=k:
                return True
            myDict[nums[i]]=i
        return False

# source: 