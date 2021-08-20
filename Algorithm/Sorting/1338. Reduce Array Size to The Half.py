# https://leetcode.com/problems/reduce-array-size-to-the-half/
# Source: Leetcode Discussion.
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        for index, count in enumerate(sorted(collections.Counter(arr).values(), reverse=True)):
            total_count += count
            #return when half of array is removed with these many elements.
            if total_count >= len(arr) // 2:
                return index + 1
        return 0