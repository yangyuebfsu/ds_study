***
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

***

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp_dict={}
        for x in nums:
            if x not in temp_dict.keys():
                temp_dict[x]=1
            else:
                temp_dict[x]+=1
        return max(temp_dict, key=temp_dict.get)


***

        nums.sort()
        s=len(nums)//2
        return nums[s]

***
            
