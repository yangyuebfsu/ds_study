***
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
***

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = {}
        i=0
        while i<len(s):
            if s[i] not in map_dict.keys():
                if t[i] in map_dict.values():
                    return False
                else:
                    map_dict[s[i]] = t[i]
            else:
                if map_dict[s[i]] == t[i]:
                    pass
                else:
                    return False
            i+=1
        return True
