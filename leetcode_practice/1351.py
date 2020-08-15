***
1351. Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1

***

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        first_neg=[]
        columns=len(grid[0])
        m=0
        while m<len(grid):
            n=0
            while n<len(grid[0]):
                if grid[m][n]<0:
                    first_neg.append(n)
                    break
                n+=1
            m+=1
        return sum([columns-x for x in first_neg])
