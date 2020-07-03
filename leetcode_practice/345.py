***
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"

***


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        index, vowels = [], []
        i = 0
        while i < len(s):
            if s_list[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                index.append(i)
                vowels.append(s_list[i])
            i += 1
        vowels.reverse()
        i = 0
        while i < len(index):
            s_list[index[i]] = vowels[i]
            i += 1
        return ''.join(s_list)
