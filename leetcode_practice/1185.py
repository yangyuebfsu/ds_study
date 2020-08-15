***
1185. Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

***

#import datetime as dt
class Solution:
    def convert_date(self, d,m,y):
        if m==2 and d==29:
            return [y,59]
        else:
            days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days=sum(days_month[0:m-1])+d-1
            if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) & (m>2) :
                return [y,days+1]
            else:
                return [y,days]
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        #return dt.datetime(year, month,day).strftime('%A')
        #today 20200525 is Monday
        today=self.convert_date(25,5,2020)
        target_date=self.convert_date(day,month,year)
        print(today, target_date)
        if today[0]<=target_date[0]:
            leap_years=0
            for y in range(today[0],target_date[0]+1):
                if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
                    leap_years+=1
            date_dif= (target_date[0]-today[0])*365+leap_years+target_date[1]-today[1]
        else:
            leap_years=0
            for y in range(target_date[0],today[0]+1):
                if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
                    leap_years+=1
            date_dif= (today[0]-target_date[0])*365+leap_years+today[1]-target_date[1]
        print(date_dif)
        print(date_dif%7)
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"][-(date_dif%7-1)]
            
