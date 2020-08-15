***
326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

***

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False;
        else:
            print(n)
            power=round( math.log(n,3),2 )
            return 3**power==n
