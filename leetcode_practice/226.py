'''226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def switch(root):
            if root == None:
                return 
            if root.left == None and root.right == None:
                return root
            root.left, root.right = root.right, root.left
            switch(root.left)
            switch(root.right)
            return root
        return switch(root)
        
