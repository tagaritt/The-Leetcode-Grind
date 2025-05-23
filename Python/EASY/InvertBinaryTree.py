"""
TASK:
Given the 'root' of a binary tree, invert the tree and return its root.

VARIABLE TYPES:
:type root: Optional[TreeNode]
:rtype: Optional[TreeNode]

EXAMPLE 1:
Input:        root = [4, 2, 7, 1, 3, 6, 9]
Output:       [4, 7, 2, 9, 6, 3, 1]

EXAMPLE 2:
Input:        root = [2, 1, 3]
Output:       [2, 3, 1]

EXAMPLE 3:
Input:        root = []
Output:       []

IMPLEMENTATION PROPOSAL:
My plan is to think of the overall tree as a root with two child nodes. In that, I'd want to move the left node into the right node's position and vice versa.
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if (root == None):
            return root
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
