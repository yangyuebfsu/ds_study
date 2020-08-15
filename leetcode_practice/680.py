""" 680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'. """


class Solution:
    def valid_one(self, s):
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] == s[j]:
                pass
            else:
                break
            i += 1
            j -= 1
        if i > j:
            return True
        else:
            return [i, j]

    def validPalindrome(self, s: str) -> bool:
        first_check = self.valid_one(s)
        if first_check == True:
            return True
        else:
            s1 = s[0:first_check[0]]+s[first_check[0]+1:]
            s2 = s[0:first_check[1]]+s[first_check[1]+1:]
            if (self.valid_one(s1) == True) | (self.valid_one(s2) == True):
                return True
            else:
                return False
