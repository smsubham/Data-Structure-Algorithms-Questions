#https://leetcode.com/problems/single-number-iii/
#https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #Pass 1 : 
        #Get the XOR of the two numbers we need to find
        diff = 0
        for num in nums:
            diff ^= num
        #Get its last set bit
        diff &= -diff
        #Pass 2 :
        rets = [0, 0] #this array stores the two numbers we will return
        for num in nums:
            if (num & diff) == 0: #the bit is not set
                rets[0] ^= num;
            else: #the bit is set
                rets[1] ^= num
        return rets