***
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

***

import collections
class Solution:
    def follow_rule(self, l):
        temp_l=[x for x in l if x!='.']
        freq=collections.Counter(temp_l)
        if any([x>1 for x in freq.values()]):
            return False
        else:
            return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if ~self.follow_rule(row):
                pass
            else:
                return False
        for i in range(0,9):
            if self.follow_rule([row[i] for row in board]):
                pass
            else:
                return False
        partitions=[range(0,3),range(3,6), range(6,9)]
        for square in [(a,b) for a in partitions for b in partitions ]:
            if self.follow_rule([board[a][b] for a in square[0] for b in square[1]]):
                pass
            else:
                return False
        return True
            
