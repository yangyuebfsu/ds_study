***
709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
***

class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
    
    
***
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        u_to_l = {
            upper[i]: lower[i]
            for i in range(0, 26)
        }
        return "".join([u_to_l[s] if s in u_to_l.keys() else s for s in str])
***
                
