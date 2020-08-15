***
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

***

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, num: int) -> bool:
        sums=[]
        path=[]
        def find_path(node):
            if node==None:
                return 
            path.append(node.val)
            if (node.left==None)&(node.right==None):
                sums.append(sum(path))    
            find_path(node.left)
            find_path(node.right)
            path.pop()
        find_path(root)
        return num in sums
