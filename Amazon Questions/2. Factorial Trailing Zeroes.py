# https://leetcode.com/problems/factorial-trailing-zeroes/
# https://practice.geeksforgeeks.org/problems/trailing-zeroes-in-factorial5134/1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        #code here 
    	five =0
    	if n<5:
    	    return 0
    	else:
            count = 1
            while n >=pow(5,count):
                five = five + math.floor(n/pow(5,count))
                count+=1
            return five
            
    	    