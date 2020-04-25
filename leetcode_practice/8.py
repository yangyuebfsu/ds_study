***
8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

***

class Solution:
    def RepresentsInt(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
    def myAtoi(self, str: str) -> int:
        #get rid of space
        i=0
        while i<len(str):
            if str[i]!=' ':
                break
            i+=1
        str=str[i:]
        if len(str)==0:
            return 0
        #handle + and - sign
        i=0
        if str[i]=='+':
            positive=True
            s=str[i+1:]
        elif str[i]=='-':
            positive=False
            s=str[i+1:]
        elif self.RepresentsInt( str[i] ):
            s=str[i:]
            positive=True
        else:
            return 0
        if len(s)==0:
            return 0
        #get only numbers
        i=0
        while i<len(s):
            if self.RepresentsInt( s[i] ):
                pass
            else:
                break
            i+=1
        s=s[:i]
        if len(s)==0:
            return 0
        output= int(s) if positive else (0-int(s))
        #check range
        if output>=2**31-1:
            return 2**31-1
        elif output<-2**31:
            return -2**31
        else:
            return output

***
            
