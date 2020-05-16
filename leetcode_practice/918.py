***
918. Maximum Sum Circular Subarray

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

***

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if max(A) <= 0: return max(A)
        max_c, max_g, min_c, min_g=A[0],A[0],A[0],A[0]
        
        for i in range(1,len(A)):
            max_c=max(A[i],max_c+A[i])
            if max_g<max_c:
                max_g=max_c
            min_c=min(A[i],min_c+A[i])
            if min_g>min_c:
                min_g=min_c
            
        return max(max_g,sum(A) - min_g)
"""
for array 12345, sum of 512 equals sum(12345)-sum(34)
"""
