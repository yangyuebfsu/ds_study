***
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

***

class Solution:
    def firstUniqChar(self, s: str) -> int:
        i=0
        temp={}
        while i<len(s):
            if s[i] not in temp.keys():
                temp[s[i]]=1
            else:
                temp[s[i]]+=1
            i+=1
        i=0
        while i<len(s):
            if temp[s[i]]==1:
                return i
            i+=1
        if i==len(s):
            return -1
