#https://leetcode.com/problems/implement-strstr/


#https://leetcode.com/problems/implement-strstr/discuss/12814/My-answer-by-Python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1