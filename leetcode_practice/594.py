***
594. Longest Harmonious Subsequence

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
***

from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_ = 0
        for key in freq.keys():
            if key+1 in freq.keys():
                if freq[key]+freq[key+1]>max_:
                    max_ = freq[key]+freq[key+1]
        return max_
            
