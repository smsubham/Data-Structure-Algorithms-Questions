#https://leetcode.com/problems/3sum-closest/
#https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
#https://www.lintcode.com/problem/59

import sys
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        n = len(numbers)
        closest = sys.maxsize
        numbers.sort()
        for i in range(n):
            left,right = i+1,n-1
            while left<right:
                sum = numbers[left] + numbers[right]+numbers[i]
                if sum == target:
                    return target
                if sum>target:
                    right -= 1
                elif sum<target:
                    left += 1
                if abs(sum - target) < abs(closest - target):
                    closest = sum
        return closest