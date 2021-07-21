# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:      
        days_31 = [1,3,5,7,8,10,12]
        date_num = date.split("-")
        #print(date_num)
        no_of_days = 0
        if int(date_num[0]) % 4 ==0:
            for i in range(1,int(date_num[1])):
                print(i)
                if i in days_31:
                    no_of_days += 31
                elif i ==2:
                    no_of_days += 29
                else:
                    no_of_days += 30
        else:
            for i in range(1,int(date_num[1])):
                if i in days_31:
                    no_of_days += 31
                elif i ==2:
                    no_of_days += 28
                else:
                    no_of_days += 30
            
        no_of_days += int(date_num[2])
        return no_of_days