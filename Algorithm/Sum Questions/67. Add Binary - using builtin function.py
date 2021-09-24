#https://leetcode.com/problems/add-binary/
#from comment section
#https://leetcode.com/problems/add-binary/discuss/24500/An-accepted-concise-Python-recursive-solution-10-lines


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]