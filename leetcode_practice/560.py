***
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

***

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l=0
        output=0
        while l<len(nums):
            r=l
            sum=0
            while r<len(nums):
                sum=sum+nums[r]
                if sum==k:
                    output+=1
                r+=1
            l+=1
        return output

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)
