***
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

***

class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            temp_list=list(str(x))
            temp_list.reverse()
            output= int( ''.join( temp_list ) )
        if x<0:
            temp_list=list(str(x)[1:])
            temp_list.reverse()
            output= -int( ''.join( temp_list ) )
        if output>2**31-1:
            return 0
        if output<-2**31:
            return 0
        else:
            return output
            
