'''
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
'''


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x = coordinates[0]
        y = coordinates[1]
        if y[0] != x[0]:
            a = (y[1]-x[1])/(y[0]-x[0])
            b = x[1] - a*x[0]
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != coordinates[i][0]*a + b:
                    return False
            return True
        else:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != x[0]:
                    return False
            return True
