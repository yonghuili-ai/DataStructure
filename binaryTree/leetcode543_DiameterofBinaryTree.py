"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 10**4].
-100 <= Node.val <= 100
"""

# time O(N) traverse N nodes
# Space O(N) The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(log⁡N).


# key points: using dfs to get the depth of subtree, at the same time, tracking the current max diameter
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 # the same as define a nonlocal variable as attached
        def depth(node):
            if not node: return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            curr_diameter = left_depth + right_depth
            # Update the maximum diameter if the current diameter is larger
            self.max_diameter = max(self.max_diameter, curr_diameter)
            # Return the height of the current node
            return 1+max(left_depth,right_depth)
        depth(root)
        return self.max_diameter

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         max_dia = 0
#         def traverse(root):
#             if not root: return 0
#             nonlocal max_dia
#             left = traverse(root.left)
#             right = traverse(root.right)
#             max_dia = max(left + right, max_dia)
#             return max(left, right) + 1   



# Example usage:
# Construct the tree [1,2,3,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3


# self.max_diameter is used to keep track of the maximum diameter found during the traversal.
# The depth function computes the depth of a node and updates the maximum diameter.
# For each node, the depth is calculated by taking the maximum depth of its left and right subtrees and adding 1.
# The diameter passing through a node is the sum of the depths of its left and right subtrees.
# self.max_diameter is updated if the current diameter is greater than the previously recorded maximum diameter.