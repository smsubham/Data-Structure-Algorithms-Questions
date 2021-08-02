#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        num =0
        #flag = 0 means +ve no
        flag =0
        if x<0:
            flag =1 #indicates -ve no
        x = abs(x)
        while x >0:
            last = x %10
            num = num*10 + last
            x = x//10
        #print(num)
        if num> (2**31)-1 or num< - (2**31):
            return 0
        
        if flag ==1:
            return -num
        return num