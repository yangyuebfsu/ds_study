'''
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

import string
CapitalLetters = list(string.ascii_uppercase)


class Solution:
    def convertToTitle(self, n: int) -> str:
        ans_list = []
        while n > 26:
            if n % 26 == 0:
                ans_list.append(26)
                n = n//26 - 1
            else:
                ans_list.append(n % 26)
                n = n//26
        ans_list.append(n)
        return ''.join([CapitalLetters[x-1] for x in reversed(ans_list)])
