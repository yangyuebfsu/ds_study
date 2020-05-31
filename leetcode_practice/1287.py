***
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

***
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq={}
        for x in arr:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
            
            if freq[x]>len(arr)/4:
                return x
