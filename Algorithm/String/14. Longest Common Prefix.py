# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count =0
        # base case
        if len(strs) ==0:
            return
        if len(strs) ==1:
            return strs[0]
        i=0
        while i< len(strs[0]) and i< len(strs[1]) and strs[0][i] == strs[1][i]:
            i += 1
        if i ==0:
            return ""
        prefix = strs[0][:i]
        for str in strs[2:]:
            #if one string is empty then longest common prefix will be empty
            # if i is zero then empty string (-1) is the answer so why continue 
            # further
            if len(str) ==0 or i==0:
                return ""
            i = min(i,len(str))
            if str[:i] != prefix:
                while i>=0 and str[i-1] != prefix[i-1]:
                    i -= 1
            prefix = prefix[:i]
        return prefix[:i]