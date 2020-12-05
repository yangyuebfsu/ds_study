'''
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(not root):   
            return []
        queue = collections.deque([root])
        all_levels = []
        while (queue): 
            size = len(queue)
            curr_level = []
            for _ in range(size):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if(curr.left):     queue.append(curr.left)
                if(curr.right):    queue.append(curr.right)
            all_levels.append(curr_level)
        return all_levels