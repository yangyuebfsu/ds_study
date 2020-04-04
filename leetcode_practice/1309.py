1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
***
import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        digit_list=[str(x)+'#' if x>9 else str(x) for x in list(range(1,27))  ]
        mapping= dict(zip(digit_list,string.ascii_lowercase) )

        output=[]
        i=0
        while i < len(s):
            print(i)
            if i<len(s)-2 :
                if s[i+2]=='#':
                    output.append(mapping[s[i:i+3]])
                    i+=3
                    continue
                else:
                    output.append(mapping[s[i]])
            else:
                output.append(mapping[s[i]])
            i+=1
        return ''.join(output)
    
# ***
#     def freqAlphabets(self, s: str) -> str:
#         for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
#         return s
# ***
