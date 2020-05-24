***
1399. Count Largest Group

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5

***

class Solution:
    def sum_digits(self, n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    def countLargestGroup(self, n: int) -> int:
        i=1
        temp_dict={}
        while i<=n:
            #temp_sum_digits=sum( [int(x) for x in list( str(i) )] )
            temp_sum_digits=self.sum_digits(i)
            if temp_sum_digits in temp_dict:
                temp_dict[temp_sum_digits]=temp_dict[temp_sum_digits]+1
            else:
                temp_dict[temp_sum_digits]=1
            i+=1
        return sum( [True for value in temp_dict.values() if value == max(temp_dict.values()) ] )
