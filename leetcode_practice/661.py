***
661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

***

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        output=[ [0 for y in range(len(M[0]))] for x in range(len(M))]
        #cant writ the output as the following
        #output=[[0]*len(M[0])]*len(M)
        #this repeat the same list for multiple times
        #once a list is modified, it applies to all repeatations.
        for x in range( len(M) ):
            for y in range( len(M[0]) ):
                temp_cells=[]
                for m in [-1,0,1]:
                    for n in [-1,0,1]:
                        if (x+m<0)|(y+n<0)|(x+m>=len(M))|(y+n>=len(M[0])):
                            pass
                        else:
                            temp_cells.append(M[x+m][y+n])
                new_value=sum(temp_cells)//len(temp_cells)
                output[x][y]=new_value
        return output
