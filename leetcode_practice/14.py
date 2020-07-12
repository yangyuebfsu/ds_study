***
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

***
class Solution:
    def common_prefix(self, str1, str2):
        i = 0
        while i<min(len(str1), len(str2)):
            if str1[i] == str2[i]:
                i+=1
            else:
                break
        return str1[:i] if i>0 else ''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        common = strs[0]
        i = 1
        while i<len(strs):
            common = self.common_prefix(common, strs[i])
            i+=1
        return common

