"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        l, r = -math.inf, math.inf
        def dfs(curr, l, r, val):
            # if curr is None:
            #     return 
            # if val > r or val < l:
            #     return 
            # if val == curr.val:
            #     return curr
            # can be simiplifed as 
            if not curr or curr.val == val: return curr
            if val > r or val < r: # not needed
                return 



            return dfs(curr.left, l, curr.val, val) or dfs(curr.right, curr.val, r, val)
        return dfs(root, l, r, val)