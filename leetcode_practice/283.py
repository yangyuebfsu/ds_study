***
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

***

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index_nonzeros=[i for i in range(len(nums)) if nums[i] !=0]
        for idx,value in enumerate(index_nonzeros):
            nums[idx]=nums[value]
        for idx in range(len(index_nonzeros), len(nums)):
            nums[idx]=0
