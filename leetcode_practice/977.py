***
977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
***
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l ,r = 0,len(A)-1
        res = []
        while l <= r:
            if A[r]**2 >= A[l]**2:
                res.append(A[r]**2)
                r -= 1
            else:
                res.append(A[l]**2)
                l += 1
        return res[::-1]
