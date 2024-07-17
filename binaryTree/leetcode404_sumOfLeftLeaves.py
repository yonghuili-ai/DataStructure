"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # to find the sum of all left leaves in a binary tree, we can traverse the tree recursively and check if each node is a left leaf. If a node is a left leaf, we add its value to the sum.

        # initialize a variable to store the sum of left leaves
        self.res = 0
        def dfs(node):
            if not node: return 
            # if the left child exists and it is a leaf node
            if node.left and node.left.left is None and node.left.right is None: 
                self.res += node.left.val
            # Recursively traverse the left and right children of the current node.
            dfs(node.right)
            dfs(node.left)

        dfs(root)
        return self.res
            
 # O(n) time
 # O(H) space, H is the height of the binary tree  