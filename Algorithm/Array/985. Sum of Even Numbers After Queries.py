#https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# Time Complexity: O(N+Q) where N is the length of A and Q is the number of queries.
#Space Complexity: O(Q)

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]: 
        queryEvenSum = []
        S = sum(x for x in nums if x%2==0)
        #print(S)
        for value,index in queries:
            #remove current number from sum
            if nums[index] % 2 == 0:
                S -= nums[index]
            nums[index] += value
            #add updated value at index if its even.
            if nums[index] %2 == 0:
                S += nums[index]
            queryEvenSum.append(S)
        return queryEvenSum