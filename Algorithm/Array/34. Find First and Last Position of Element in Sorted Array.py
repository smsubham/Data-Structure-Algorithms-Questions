#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)


class Solution:
    def searchRange(self, A: List[int], target: int) -> List[int]:
        n = len(A)
        i,j = 0,n - 1
        ret = [-1, -1]
        if n<=0: return [-1,-1]
        #Search for the left one
        while i < j:
            mid = (i + j) //2
            if A[mid] < target: i = mid + 1
            else: j = mid
        if A[i]!=target: return ret
        else: ret[0] = i
        #Search for the right one
        j = n-1  #We don't have to set i to 0 the second time.
        while i < j:
            mid = (i + j) //2 + 1	#Make mid biased to the right
            if A[mid] > target: j = mid - 1  
            else: i = mid				#So that this won't make the search range stuck.
        ret[1] = j
        return ret