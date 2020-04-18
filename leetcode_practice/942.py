***
942. DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
***

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        start=len(S)-len([x for x in list(S) if x=='I'])
        i=0
        A=[start]
        up=start
        down=start
        while i<len(S):
            if S[i]=='D':
                down=down-1
                A.append( down )
            else:
                up=up+1
                A.append( up )
            i+=1
        return A