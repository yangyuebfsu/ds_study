***
500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

***

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 ="qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        row_dict={}
        for x in list(row1):
            row_dict[x]=1
            row_dict[x.upper()]=1
        for x in list(row2):
            row_dict[x]=2
            row_dict[x.upper()]=2
        for x in list(row3):
            row_dict[x]=3
            row_dict[x.upper()]=3
        output=[]
        for word in words:
            i=0
            while i<len(list(word))-1:
                if row_dict[word[i]]!=row_dict[word[i+1]]:
                    break
                i+=1
            if i==len(list(word))-1:
                output.append(word)
        return output
