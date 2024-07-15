"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time O(n), we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
# space O(N)-O(logN), in worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recurrsion call would occur N times. In the best case, when the tree is completely balanced, the height of the tree is O(logN). 

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

# Helper function to build a tree from a list

def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    index = 1
    while index < len(lst):
        node = queue.pop(0)
        if lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)
        index += 1
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)
        index += 1
    return root

# Example usage:
tree_list1 = [3, 9, 20, None, None, 15, 7]
root1 = build_tree_from_list(tree_list1)
print(maxDepth(root1))  # Output: 3

tree_list2 = [1, None, 2]
root2 = build_tree_from_list(tree_list2)
print(maxDepth(root2))  # Output: 2



