"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10**7
root is a binary search tree.
1 <= val <= 10**7

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif val > root.val:
            # r = self.searchBST(root.right, val) can not define like this, since r could never be visited, and r is not associated with a value
            return self.searchBST(root.right, val) # directly return from the root's right subtree
        elif val < root.val:
            # l = self.searchBST(root.left, val) # same error as r, UnboundLocalError: cannot access local variable 'r' where it is not associated with a value
            return self.searchBST(root.left, val)




# time O(h) h could be logn to n, logn is for completely balanced tree, n is completely not balanced tree

# space O(h) recursion call takes h space