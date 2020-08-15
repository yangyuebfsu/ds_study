***
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

***

bracket_dict={'(':')','[':']','{':'}'}
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        s=list(s)
        left_bracket_loc=[]
        i=0
        while i<len(s):
            if s[i] in bracket_dict.keys():
                left_bracket_loc.append(i)
            i+=1
        for i in reversed(left_bracket_loc):
            if i+1>=len(s):
                return False
            elif s[i+1]==bracket_dict[s[i]]:
                s.pop(i+1)
                s.pop(i)
                continue
            else:
                return False
        return True


***stack is not that fast***
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for c in s:
          if c in d.values():
            stack.append(c)
          elif not stack or stack.pop() != d[c]:
              return False
        return True if not stack else False



