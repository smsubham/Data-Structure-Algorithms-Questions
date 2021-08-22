# https://leetcode.com/problems/string-compression/

# source: https://leetcode.com/problems/string-compression/discuss/282239/Python-Two-Pointers-Solution-Easy-To-Understand-O(1)-space
#Time: O(n), Space: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        #walker => points to the char array and helps in storing the characer and counts.
        #runner => points to the next character to be counted.
        walker, runner = 0, 0
        while runner < len(chars):
            #store character to be counted
            chars[walker] = chars[runner]
            #already 1 char encountered, see if we have more of same character adjacent.
            count = 1
            #keep count of number of adjacent character
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1
            #if count is greater than 1
            if count > 1:
            #line 6 stored the character, this line stores count, suppose we have 129 count
            #then it will store it as 1,2,9 as separate character as we have convrted it
            #to string  and then iterating each digit one by one and storing.
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            #we need to move runner and walker to point to next character
            runner += 1
            walker += 1
        print(chars)
        return walker