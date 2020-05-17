***
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

***

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import collections
class Solution:
    def dict_greater(self, dict1,dict2):
        if [x for x in dict1.keys() if x not in dict2.keys()]:
            return True
        elif any([dict1[key]>dict2[key] for key in dict1.keys()]):
            return True
        else:
            return False
    def dict_plus(self, dict_temp,x):
        if x in dict_temp:
            dict_temp[x]+=1
        else:
            dict_temp[x]=1
        return dict_temp
    
    def dict_minus(self, dict_temp,x):
        if x not in dict_temp:
            return dict_temp
        if dict_temp[x]>1:
            dict_temp[x]=dict_temp[x]-1
        else:
            del dict_temp[x]
        return dict_temp
            
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i=0
        dict_p=collections.Counter(p)
        index=0
        dict_temp={}
        output=[]
        while i<len(s):
            dict_temp=self.dict_plus(dict_temp,s[i])
            while self.dict_greater(dict_temp,dict_p):
                dict_temp=self.dict_minus(dict_temp,s[index])
                index=index+1
            if dict_temp==dict_p:
                output.append(i)
            i+=1
        return [x-len(p)+1 for x in output]
