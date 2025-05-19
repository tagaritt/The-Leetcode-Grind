"""
TASK:
You are given the 'root' of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
Return 'true' if the value of the root is equal to the sum of the values of its two children, or 'false' otherwise.

VARIABLE TYPES:
:type root: Optional[TreeNode]
:rtype: bool

EXAMPLE 1:
Input:        root = [10, 4, 6]
Output:       true
Explanation:  The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
              10 is equal to 4 + 6, so we return true.

EXAMPLE 2:
Input:        root = [5, 3, 1]
Output:       false
Explanation:  The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
              5 is not equal to 3 + 1, so we return false.

IMPLEMENTATION PROPOSAL:
The plan is to add the two children nodes and try to equate their sum to the root. If they are equal, the program should return a true value and if they aren't the program should return a false.
"""

### Definition for a binary tree node. ###
class TreeNode(object):
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

### LeetCode Implementation ###
class Solution(object):
  def checkTree(self, root: Optional[TreeNode]) -> bool:
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    return (root.val == root.left.val + root.right.val)

### Actual Implementation ###
class Solution(object):
    def checkTree(self, root: TreeNode) -> bool:
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return (root.val == root.left + root.right)

# 'XX' can be any integer value
root = TreeNode(val = XX, left = XX, right = XX)

print(Solution().checkTree(root))
