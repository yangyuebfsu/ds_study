***
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

***

import collections
r_dict={'IV':'I'*4,
         'IX':'I'*9,
         'XL':'X'*4,
         'XC':'X'*9,
         'CD':'C'*4,
         'CM':'C'*9,
        }
value_dict={'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
           }
class Solution:
    def romanToInt(self, s: str) -> int:
        for key in r_dict:
            s=s.replace(key, r_dict[key])
        freq=collections.Counter(s)
        return sum([freq[x]*value_dict[x] for x in freq])
