'''572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,s,t):
        if s is None and t is None:
            return True
        elif s is not None and t is not None:
            return (s.val==t.val) and \
        (self.isSame(s.left,t.left)) and \
        (self.isSame(s.right,t.right))
        else:
            return False
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        temp = []
        temp_value = t.val
        def check(root):
            if root is None:
                return 
            check(root.left)
            check(root.right)
            if root.val == temp_value:
                temp.append(root)
            else:
                pass
        check(s)
        return any([self.isSame(t,x) for x in temp])
