***
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

***

import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

class Solution:

    def climbStairs(self, n: int) -> int:
        x=0
        count=0
        while 2*x<=n:
            y=n-2*x
            count+=nCr( (x+y) , x) 
            x+=1
        return int( count )
    
***
def climbStairs(self, n: int) -> int:
    if n < 3: return n
	else: return self.climbStairs(n-1) + self.climbStairs(n-2)
***
