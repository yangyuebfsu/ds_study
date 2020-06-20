***
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

***

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dict1, dict2 = {}, {}
        list_str = str.split(' ')
        if len(pattern)!=len(list_str):
            return False
        i = 0
        while i<len(pattern):
            if pattern[i] not in dict1.keys():
                if list_str[i] not in dict2.keys():
                    dict1[pattern[i]] = list_str[i]
                    dict2[list_str[i]] = 1
                else:
                    return False
            else:
                if dict1[pattern[i]] == list_str[i]:
                    pass
                else:
                    return False
            i+=1
        return True
