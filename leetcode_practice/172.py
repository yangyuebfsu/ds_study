***
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

***

class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=0
        while 5**i<=n:
            i+=1
        return sum([n//(5**x) for x in range(1,i)])
