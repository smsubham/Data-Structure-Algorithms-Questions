#https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        temp = []
        for i in range(len(nums)):
            freq[nums[i]]+=1
            #print(freq[nums[i]])
        #print(freq[0])
        #print(freq[1])
        #print(freq[2])
        for i in range(freq[0]):
            nums[i]=0
            #print(0)
        for i in range(freq[0],freq[0]+freq[1]):
            nums[i]=1
            #print(1)
        for i in range(freq[1]+freq[0],freq[0]+freq[1]+freq[2]):
            nums[i]=2
            #print(2)
        print(nums)
        #nums[:] = list(nums)