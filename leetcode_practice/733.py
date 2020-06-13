***
733. Flood Fill
Easy

1121

190

Add to List

Share
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

***

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        area=[]
        oldColor=image[sr][sc]
        def search_area(x,y):
            if ( [x,y] in area)|(x<0)|(x>len(image)-1)|(y<0)|(y>len(image[0])-1):
                return
            elif image[x][y]!=oldColor:
                return
            else:
                area.append([x,y])
                search_area(x-1,y)
                search_area(x+1,y)
                search_area(x,y-1)
                search_area(x,y+1)
        search_area(sr,sc)
        for point in area:
            image[point[0]][point[1]]=newColor
        return image
            
