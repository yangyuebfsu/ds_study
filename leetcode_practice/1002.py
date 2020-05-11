***
1002. Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

***

import collections
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        temp=collections.Counter(A[0])
        for x in A[1:]:
            for key, value in temp.items() :
                freq=x.count(key)
                if freq<value:
                    temp[key]=freq
            temp={x:y for x,y in temp.items() if y!=0}
        output=[]
        for x, y in temp.items():
            output=output+[x]*y
        return output
            
