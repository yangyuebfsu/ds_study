***
581. Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
***

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #get the first non ascending point
        i=0
        while i<len(nums)-1:
            if nums[i+1]<nums[i]:
                break
            i+=1
        #if all ascending, return 0
        if i == len(nums)-1:
            return 0
        #get the last non ascending point
        j=len(nums)-1
        while j>1:
            if nums[j-1]>nums[j]:
                break
            j-=1
        #the final subarray must at least include the following
        temp_list = nums[i:j+1]
        
        #the final subarray might include more if current min and max are too extreme
        min_, max_ = min(temp_list), max(temp_list)
        #extend the final subarray
        i=0
        while i<len(nums)-1:
            if nums[i]>min_:
                break
            i+=1
        j=len(nums)-1
        while j>1:
            if nums[j]<max_:
                break
            j-=1
        return j-i+1
            
