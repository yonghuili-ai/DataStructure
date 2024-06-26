# 插入一个数，就是先找到插入位置，然后进行插入操作。
# https://labuladong.online/algo/data-structure/bst-part2/#div_insert-into-a-binary-search-tree

# trickly part is how to attach the new node to existing tree? 
# see answers below.
"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 10**4].
-10**8 <= Node.val <= 10**8
All the values Node.val are unique.
-10**8 <= val <= 10**8
It's guaranteed that val does not exist in the original BST.

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val) # when the node is None, means found the location to insert TreeNode(val). And this will attach to the 1 level up node's left or right side.
        if val > root.val: 
            root.right = self.insertIntoBST(root.right, val) # must have root.right = xxxx for attaching the newNode to existing root subtree 
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # at last, return the whole tree root
        return root

# time O(h) h is the height of the tree, checked logn element if completely balance, worst case n nodes if completely not balanced

# space O(h), recursion happend in h level stack
        