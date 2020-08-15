'''
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        first, pattern = s[0], [s[0]]
        i = 1
        while i < len(s)/2+1:
            if s[i] == first:
                times = len(s)//len(pattern)
                temp = ''.join(pattern)*times
                if temp == s:
                    return True
            pattern.append(s[i])
            i += 1
        return False
