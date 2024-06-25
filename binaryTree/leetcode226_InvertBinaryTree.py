# solution idea from https://labuladong.online/algo/data-structure/binary-tree-part1/
"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # traverse method
        # def traverse(node):
        #     if not node: return None
        #     node.left, node.right = node.right, node.left 
        #     traverse(node.left)
        #     traverse(node.right)
        # traverse(root)
        # return root 
    
        # divide and conquer
        if not root: return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left 
        return root 


# time O(n) traverse each node once 
# space O(logn-n) completly balanced O(logn), not balance O(n)