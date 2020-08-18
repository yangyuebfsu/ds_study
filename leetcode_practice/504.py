'''
504. Base 7

Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"
Example 2:

Input: -7
Output: "-10"
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        neg = True if num < 0 else False
        num = abs(num)

        while num >= 7:
            ans.append(num % 7)
            num = num//7
        ans.append(num)

        ans = ''.join(reversed([str(x) for x in ans]))
        return '-'+ans if neg else ans
