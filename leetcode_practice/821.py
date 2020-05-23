***
821. Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

***
class Solution:
    def min_dist(self, loc,index):
        if loc<=index[0]:
            return index[0]-loc
        elif loc>=index[-1]:
            return loc-index[-1]
        else:
            i=0
            while i<len(index):
                if index[i]>loc:
                    break
                i+=1
            return min(index[i]-loc,loc-index[i-1])
                    
    def shortestToChar(self, S: str, C: str) -> List[int]:
        i=0
        index=[]
        while i<len(S):
            if S[i]==C:
                index.append(i)
            i+=1
        return [self.min_dist(x, index) for x in range(len(S))]
