***
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. 
Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]. 
Note: The length of path between two nodes is represented by the number of edges between them. 

***

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, node):
        # base case:
        if node == None:
            return 0
		# recursive cases
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.diameter = max(self.diameter,left_height + right_height )
        return max(left_height,right_height) + 1
    '''
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1+self.diameterOfBinaryTree(root.right)
        if  root.left and not root.right:
            return 1+self.diameterOfBinaryTree(root.left)
        else:
            return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))+1
        '''
        
***