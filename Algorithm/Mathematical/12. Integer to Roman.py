# https://leetcode.com/problems/integer-to-roman/
# https://practice.geeksforgeeks.org/problems/convert-to-roman-no/1
#Credit: https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution 
# More Solutions: https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/

class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10];