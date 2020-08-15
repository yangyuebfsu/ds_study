'''687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_length = 0
        def dfs(root):
            if not root:
                return 0
            l= dfs(root.left)
            r= dfs(root.right)    
            l = 1 + l if root.left and root.left.val == root.val else 0
            r = 1 + r if root.right and root.right.val == root.val else 0
            self.max_length = max(self.max_length, l+r)
            return max(l, r)
        dfs(root)
        return self.max_length
        
