***
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
***

class Solution:

    # def rob(self, nums: List[int]) -> int:   
    # recursion exceed time limits
    #     if len(nums)==0:
    #         return 0
    #     elif len(nums)==1:
    #         return nums[0]
    #     elif len(nums)==2:
    #         return max([nums[0], nums[1]])
    #     elif len(nums)==3:
    #         return max([(nums[0]+nums[2]), nums[1]])
    #     else:
    #         first=nums[0]+self.rob( nums[2:])
    #         second=nums[1]+self.rob( nums[3:])
    #         return max([first,second])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            to_n_2 = 0 # biggest sum up to (n-2)
            to_n_1 = nums[0] # biggest sum up to (n-1)
            i=1
            while i<len(nums):
                n_2_and_n=to_n_2+nums[i] # [biggest sum up to (n-2)] + n
                to_n=max(n_2_and_n,to_n_1) # compared with biggest sum up to (n-1), get biggest sum to n
                to_n_2=to_n_1
                to_n_1=to_n
                i+=1
            return to_n
