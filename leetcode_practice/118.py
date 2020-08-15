***
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

***

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        i=3
        lastrow=[1,1]
        output=[[1],[1,1]]
        while i<=numRows:
            newrow=[1]+[lastrow[i]+lastrow[i+1] for i in range(len(lastrow)-1)] + [1]
            output.append(newrow)
            lastrow=newrow
            i+=1
        return output
