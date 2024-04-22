# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # to find all possible permutations of BST with n nodes, we can lock one node as the root node, and split n-1 nodes between the left and right subtrees in all possible ways. Let's say we place a node with value i as the root node and place i-1 nodes having values from 1 to i-1 in the left subtree. (if i=1, the left child is null). Similarly, we place the remaining n-1 nodes having values from i+1 to n in the right subtree. (if i == n, the right child is null).
        # https://www.youtube.com/watch?v=HeB6Oufsg_o&t=438s


# still do not quite understand!