***
1162. As Far from Land as Possible

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

***

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        lands = [(x, y) for x in range(r) for y in range(c) if grid[x][y]==1]
        n_visited, n_total = len(lands), r*c
        if (n_visited==0)|(n_visited==n_total):
            return -1
        visited = set( lands )
        level = 1
        while n_visited<n_total:
            level += 1
            to_be_visited = set()
            for m, n in visited:
                for a, b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    to_be_visited.add((m+a,n+b))
            for x, y in to_be_visited:
                if ( (x, y) in visited ) | ( (x<0)|(x>r-1)|(y<0)|(y>c-1) ):
                    continue
                if grid[x][y]==0:
                    visited.add((x,y))
                    n_visited +=1
                    grid[x][y] = level
        return level-1



