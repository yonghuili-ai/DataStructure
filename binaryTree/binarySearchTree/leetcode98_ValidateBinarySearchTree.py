"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true


Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

The number of nodes in the tree is in the range [1, 10**4].
-2**31 <= Node.val <= 2**31 - 1
"""

# 对于某一个节点 root，他只能管得了自己的左右子节点，怎么把 root 的约束传递给左右子树呢？
# ==>
# 限定左子树的最大值是 root.val，右子树的最小值是 root.val

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, mi=-float('inf'), ma=float('inf')): # initially the root node has no min, max requirement
            if not node: return True
            # should not defined here, since you can not pass mi, ma to next traverse!
            # should define within the traverse function valid(node.left, mi, node.val)
            # mi = max of node.left ?
            # ma = min of node.right ?
            if not (mi < node.val < ma): # other than this condition, all rest should be False
                return False
        # left_valid = valid(root.left, -float('inf'), root.val) # should not set here, but should give a default value in original traverse function definition
        # right_valid = valid(root.right, root.val, float('inf'))
            left_valid = valid(node.left, mi, node.val)
            right_valid = valid(node.right, node.val, ma)
            return left_valid & right_valid

        return valid(root)

# time O(N) checked on each node onces, takes O(N)

# space O(logN - N) height of the stack for traverse, or bst height


# Example usage:
# Construct the tree [2, 1, 3]
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

sol = Solution()
print(sol.isValidBST(root1))  # Output: true

# Construct the tree [5, 1, 4, null, null, 3, 6]
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(sol.isValidBST(root2))  # Output: false